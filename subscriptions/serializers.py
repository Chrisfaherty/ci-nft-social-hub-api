from rest_framework import serializers
from subscriptions.models import Subscribers, SubscribersMessage


class SubscribersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')
    email = serializers.EmailField()

    class Meta:
        model = Subscribers
        fields = [
            'id', 'owner', 'created_at', 'email', 'date'
        ]


class SubscribersMessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')
    title = serializers.CharField()
    message = serializers.CharField()

    class Meta:
        model = Subscribers
        fields = [
            'id', 'owner', 'created_at', 'title', 'message'
        ]