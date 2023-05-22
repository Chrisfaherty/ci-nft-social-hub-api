from rest_framework import generics, permissions
from nft_social_hub_api.permissions import IsOwnerOrReadOnly
from subscriptions.models import Subscribers, SubscribersMessage
from subscriptions.serializers import SubscribersSerializer, SubscribersMessageSerializer


class SubscribersList(generics.ListCreateAPIView):
    serializer_class = SubscribersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subscribers.objects.all()

    def perform_create(self, serializer):
        serializer.save(fullname=self.request.user)

 
class SubscribersDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SubscribersSerializer
    queryset = Subscribers.objects.all()


class SubscribersMessageList(generics.ListCreateAPIView):
    serializer_class = SubscribersMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SubscribersMessage.objects.all()

    def perform_create(self, serializer):
        serializer.save(fullname=self.request.user)


class SubscribersMessageDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SubscribersMessageSerializer
    queryset = SubscribersMessage.objects.all()
