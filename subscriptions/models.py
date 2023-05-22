from django.db import models


class Subscribers(models.Model):
    fullname = models.CharField(max_length=55)
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['fullname', 'email']

    def __str__(self):
        return f'{self.fullname} {self.email}'


class SubscribersMessage(models.Model):
    fullname = models.CharField(max_length=55)
    email = models.EmailField(null=True)
    title = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)

    class Meta:
        unique_together = ['fullname', 'email']

    def __str__(self):
        return f'{self.fullname} {self.email}'
