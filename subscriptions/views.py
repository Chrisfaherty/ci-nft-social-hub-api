from rest_framework import generics
from subscriptions.models import Subscribers, SubscribersMessage
from subscriptions.serializers import SubscribersSerializer, SubscribersMessageSerializer


class SubscribersList(generics.ListCreateAPIView):
    serializer_class = SubscribersSerializer
    queryset = Subscribers.objects.all()


class SubscribersDetail(generics.RetrieveDestroyAPIView):
    serializer_class = SubscribersSerializer
    queryset = Subscribers.objects.all()


class SubscribersMessageList(generics.ListCreateAPIView):
    serializer_class = SubscribersMessageSerializer
    queryset = SubscribersMessage.objects.all()


class SubscribersMessageDetail(generics.RetrieveDestroyAPIView):
    serializer_class = SubscribersMessageSerializer
    queryset = SubscribersMessage.objects.all()
