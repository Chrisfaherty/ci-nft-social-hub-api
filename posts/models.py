from django.db import models
from django.contrib.auth.models import User
from ratings.models import Rating
from django.db.models import Avg


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    category_choices = [
    ('pfps / avatars', 'PFPs / Avatars'),
    ('one-of-one artwork', 'One-of-one Artwork'),
    ('generative art', 'Generative art'),
    ('collectibles', 'Collectibles'),
    ('photography', 'Photography'),
    ('music', 'Music'),
    ('gamified', 'Gameified'),
    ('event ticket', 'Event Ticket'),
    ('membership pass', 'Membership Pass'),
    ('domain names', 'Domain names'),
    ('other', 'Other')

]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', 
        default='../ci-nft-social-hub/default_post_icenjp.jpg', 
        blank=True
    )
    category_filter = models.CharField(
        max_length=32, 
        choices=category_choices, 
        default='normal'
    )
    website = models.URLField(blank=True)
    social = models.URLField(blank=True)
    marketplace = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f'{self.id} {self.title} {self.average_rating()}'