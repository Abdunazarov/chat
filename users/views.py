from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q



def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            already_exists = True
            return render(request, 'users/signup.html', {'already_exists': already_exists})

        user = User.objects.create(
            username=username,
            first_name=request.POST['first_name'],
            second_name=request.POST.get('second_name'),
        )
        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/')

    return render(request, 'users/signup.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user == None:
            return render(request, 'users/login.html', {'dont_exist': True})

        login(request, user)

        return redirect('/')
    
    return render(request, 'users/login.html')


def logout_view(request):

    if request.method == 'GET':
        logout(request)

        return render(request, 'users/logout.html')



#https://docs.djangoproject.com/en/4.1/topics/db/search/

def add_contact(request):

    all_users = User.objects.all()

    if request.method == 'POST':
        input_value = request.POST.get('search_value')
        
        all_users = User.objects.filter(
        Q(username__contains=input_value) 
        | Q(first_name__contains=input_value) 
        | Q(second_name__contains=input_value))


    return render(request, 'users/add_contact.html', {'all_users': all_users})




def profile(request):

    return render(request, 'users/profile.html', {'user': request.user})


def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        if request.FILES.get('image'): 
            user.image = request.FILES['image']

        user.first_name = request.POST['first_name']
        user.second_name = request.POST.get('second_name')
        user.username = request.POST['username']
        user.phone_number = request.POST.get('phone_number')
        user.bio = request.POST.get('bio')
        user.save()
        return redirect('/auth/profile/') 

    return render(request, 'users/edit_profile.html', {'user': user})
