from rest_framework import serializers
from subscriptions.models import Subscribers, SubscribersMessage


class SubscribersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribers
        fields = [
            'id', 'fullname', 'created_at', 'email', 'date'
        ]


class SubscribersMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribersMessage
        fields = [
            'id', 'fullname', 'created_at', 'title', 'message', 'email',
        ]