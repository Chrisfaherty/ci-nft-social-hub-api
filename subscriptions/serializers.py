from rest_framework import serializers
from subscribers.models import Subscribers, SubscribersMessage

class SubscribersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.EmailField()

    class Meta:
        model = Subscribers
        fields = [
            'id', 'owner', 'created_at', 'email', 'date'
        ]


class SubscribersMessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    title = serializers.CharField()
    message = serializers.TextField()

        class Meta:
        model = Subscribers
        fields = [
            'id', 'owner', 'created_at', 'title', 'message'
        ]