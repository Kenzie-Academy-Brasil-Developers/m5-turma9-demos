from rest_framework import serializers

from .models import Floor, Spot, SpotType


class FloorSerializer(serializers.ModelSerializer):
    motorcycle_spots = serializers.IntegerField(write_only=True)
    car_spots = serializers.IntegerField(write_only=True)

    class Meta:
        model = Floor
        # fields = "__all__"
        fields = ["id", "name", "spot_priority", "car_spots", "motorcycle_spots"]
        # fields = ["id", "name", "spot_priority", "spots"]

    def create(self, validated_data):
        """
        validated_data =
        {
            "name": "floor 3",
            "spot_priority": 2,
            "motorcycle_spots": 20,
            "car_spots": 50
        }
        """
        motorcycle_spots: int = validated_data.pop("motorcycle_spots")
        car_spots: int = validated_data.pop("car_spots")

        floor = Floor.objects.create(**validated_data)

        for _ in range(motorcycle_spots):
            """INSER INTO"""
            Spot.objects.create(floor=floor, variety=SpotType.MOTORCYCLE)
            # Spot.objects.create(floor=floor, variety="motorcycle")

        for _ in range(car_spots):
            Spot.objects.create(floor=floor, variety=SpotType.CAR)

        return floor
