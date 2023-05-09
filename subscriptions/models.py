from django.db import models
from django.contrib.auth.models import User


class Subscribers(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} {self.email}


class SubscribersMessage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)

    def __str__(self):
        return f'{self.owner} {self.title}'
