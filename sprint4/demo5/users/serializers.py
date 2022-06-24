from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "password", "email", "age"]
        extra_kwargs = {"password": {"write_only": True}}
        # exclude = ["password"]

    # password = serializers.CharField(write_only=True)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    # create modelSerializer -> return User.objects.create(**validated_data)


# class RegisterSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     email = serializers.EmailField(max_length=100)
#     age = serializers.IntegerField()
#     password = serializers.CharField(write_only=True)

#     def validate_email(self, value):
#         if User.objects.filter(email__iexact=value).exists():
#             raise serializers.ValidationError("email já existe")

#         return value

#     def create(self, validated_data: dict) -> User:
#         return User.objects.create_user(**validated_data)
#         return User.objects.create_user(**validated_data)

#     def update(self, instance: User, validated_data: dict) -> User:
#         instance.email = validated_data.get("email", instance.email)
#         instance.age = validated_data.get("age", instance.age)
#         password = validated_data.get("password")

#         if password:
#             instance.set_password(password)

#         instance.save()

#         return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True)
