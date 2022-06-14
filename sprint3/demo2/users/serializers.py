from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=100)
