from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from django.contrib.auth import get_user_model

from .models import Message, RoomUsers
from users.models import User

User = get_user_model()


class ChatConsumer(WebsocketConsumer):


    def load_messages(self, data=None):
        last_10_messages = Message.last_10_messages(self.group_name)
        last_10_messages = [message for message in last_10_messages]
        last_10_messages.reverse()

        data = {'messages': []}
        for message in last_10_messages:
            dic = {
                'content': message.content,
                'author': message.user.username,
            }
            data['messages'].append(dic)

        self.send(text_data=json.dumps(data))


    def new_message(self, data):
        message = data['message']

        room = RoomUsers.objects.get(slug=self.group_name)
        user = User.objects.get(username=self.scope['user'])
        message = Message.objects.create(
            room=room,
            user=user,
            content=message
        )

        data = {
            'command': 'new_message',
            'content': message.content,
            'author': message.user.username
        }


        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat_message',
                'data': data
            }
        )



    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['slug']

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        self.load_messages()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )


    def receive(self, text_data=None):
        data = json.loads(text_data)
        print(data)

        if data['command'] == 'new_message':
            self.new_message(data)        



    def chat_message(self, event):
        data = event['data']

        self.send(text_data=json.dumps({
            'content': data['content'],
            'author': data['author'],
            'command': 'new_message'
        }))
