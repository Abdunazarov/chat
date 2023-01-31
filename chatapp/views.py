from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RoomUsers
from users.models import User
from django.db.models import Q # for multiple condition filtering



@login_required
def home(request):
    users_rooms = RoomUsers.objects.filter(Q(user1=request.user) | Q(user2=request.user))
    searched_rooms = []

    if request.method == 'POST':
        search_value = request.POST['search']
        for room in users_rooms:
            if search_value in str(room):
                searched_rooms.append(room)
        
        users_rooms = searched_rooms

    return render(request, 'chatapp/home.html', {'users_rooms': users_rooms})


def chat(request, slug):
    room = RoomUsers.objects.get(slug=slug)
    other_user = User.objects.get(username=room.user1.username)

    if request.user.username == room.user1.username:
        other_user = User.objects.get(username=room.user2.username)
        

    context = {
        'room_slug': room.slug,
        'other_user': other_user
        
    }

    return render(request, 'base.html', context)


def redirect_or_create(request, slug):
    usernames = slug.split('-')
    username1 = usernames[0]
    username2 = usernames[1]

    user1 = User.objects.get(username=username1)
    user2 = User.objects.get(username=username2)


    room = ''

    room1 = RoomUsers.objects.filter(user1=user1, user2=user2)
    room2 = RoomUsers.objects.filter(user1=user2, user2=user1)

    if room1.exists():
        room = room1[0]
    
    elif room2.exists():
        room = room2[0]

    else:
        room = RoomUsers.objects.create(user1=user1, user2=user2, slug=user1.username+user2.username)

    return redirect(f"/chat/{room.user1.username}{room.user2.username}")




def search(request, value):
    pass