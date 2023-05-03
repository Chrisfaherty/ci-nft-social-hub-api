from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('?')
    serializer_class = PostSerializer