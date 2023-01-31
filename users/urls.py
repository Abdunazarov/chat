from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signup_view, name='signup_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),

    path('add_contact/', add_contact, name='add_contact'),
    path('profile/', profile, name='profile'),
    path('edit/', edit_profile, name='edit')
]