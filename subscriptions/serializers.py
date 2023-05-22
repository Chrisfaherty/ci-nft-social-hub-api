from rest_framework import serializers
from subscriptions.models import Subscribers, SubscribersMessage


class SubscribersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribers
        fields = [
            'id', 'fullname', 'email', 'date'
        ]


class SubscribersMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribersMessage
        fields = [
            'id', 'fullname', 'title', 'message', 'email',
        ]