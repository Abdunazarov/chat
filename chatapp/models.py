from django.db import models
from users.models import User

    

class RoomUsers(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_room')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE,)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.user1.username + '-' + self.user2.username

class Message(models.Model):
    room = models.ForeignKey(RoomUsers, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username + ' - ' + self.content[0:30]

    def last_10_messages(room_slug):
        room = RoomUsers.objects.get(slug=room_slug)
        return Message.objects.filter(room=room).all().order_by('-timestamp')[:10]