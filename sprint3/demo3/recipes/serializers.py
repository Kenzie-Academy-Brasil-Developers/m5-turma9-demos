from rest_framework import serializers
from users.serializers import UserSerializer


class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(read_only=True)
    instructions = serializers.CharField(read_only=True)

    user = UserSerializer(read_only=True)

    # user = models.ForeignKey(
    #     "users.User", on_delete=models.CASCADE, related_name="recipes"
    # )
