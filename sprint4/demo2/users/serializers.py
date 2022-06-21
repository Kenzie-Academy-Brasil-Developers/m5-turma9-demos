from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=100)
    age = serializers.DateField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("email já existe")

        return value

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True)
