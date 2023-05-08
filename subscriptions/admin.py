from django.contrib import admin
from . models import Subscribers, SubscribersMessage

# Register your models here.

admin.site.register(Subscribers)
admin.site.register(SubscribersMessage)
