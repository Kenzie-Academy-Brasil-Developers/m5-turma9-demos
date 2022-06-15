from rest_framework import serializers


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)

    # recipes = serializers.ManyToManyField("recipes.Recipe", related_name="ingredients")
