from django.contrib import admin
from .models import Message, RoomUsers



admin.site.register([Message, RoomUsers])