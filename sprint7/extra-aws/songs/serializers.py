from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # duration = serializers.IntegerField(required=False)

    class Meta:
        model = Song
        fields = "__all__"
