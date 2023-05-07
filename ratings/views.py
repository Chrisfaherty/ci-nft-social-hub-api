from django.shortcuts import render
from rest_framework import generics, permissions
from ratings.serializers import RatingSerializer
from ratings.models import Rating
from posts.models import Post
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    for post in posts:
        rating = Rating.objects.filter(post=post, user=request.user).first()
        post.user_rating = rating.rating if rating else 0
    return render(request, "index.html", {"posts": posts})


def rating(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return index(request)


