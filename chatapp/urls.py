from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('chat/<slug>/', chat, name='chat'),
    path('redirect_or_create/<slug>/', redirect_or_create, name='redirect_or_create'),

    path('search/<value>/', search, name='search')
]