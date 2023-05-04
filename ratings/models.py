from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", related_name = 'ratings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.post.header} {self.rating}'
