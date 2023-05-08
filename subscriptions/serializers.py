from rest_framework import serializers

class SubscribersSerializer(serializers.Serializer):
    email = serializers.EmailField()
    date = serializers.DateTimeField()


class SubscribersMessageSerializer(serializers.Serializer):
    title = serializers.CharField()
    message = serializers.TextField()