from rest_framework import generics, permissions
from nft_social_hub_api.permissions import IsOwnerOrReadOnly
from likes.models import Like, DisLike
from likes.serializers import LikeSerializer, DisLikeSerializer


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class DisLikeList(generics.ListCreateAPIView):
    serializer_class = DisLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = DisLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DisLikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DisLikeSerializer
    queryset = DisLike.objects.all()
