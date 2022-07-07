from rest_framework import serializers

from .models import Floor, Spot, SpotType


class FloorSerializer(serializers.ModelSerializer):
    motorcycle_spots = serializers.IntegerField(write_only=True)
    car_spots = serializers.IntegerField(write_only=True)

    class Meta:
        model = Floor
        fields = [
            "id",
            "name",
            "spot_priority",
            "car_spots",
            "motorcycle_spots",
            "available_spots",
            # "churros",
        ]

    available_spots = serializers.SerializerMethodField()
    # churros = serializers.SerializerMethodField()

    # def get_churros(self, obj):
    #     return "um churros"

    # nome do método get_nome_do_atributo
    def get_available_spots(self, floor: Floor):
        # TODO:
        # trazer somente as vagas não ocupadas

        # SELECT COUNT(*) from floors_spot where floor_id=1 and variety='motorcycle';
        available_motorcycle_spots = floor.spots.filter(
            variety=SpotType.MOTORCYCLE, vehicle=None
        ).count()

        # SELECT COUNT(*) from floors_spot where floor_id=1 and variety='car';
        available_car_spots = floor.spots.filter(
            variety=SpotType.CAR, vehicle=None
        ).count()

        return {
            "available_motorcycle_spots": available_motorcycle_spots,
            "available_car_spots": available_car_spots,
        }

    def create(self, validated_data):

        motorcycle_spots: int = validated_data.pop("motorcycle_spots")
        car_spots: int = validated_data.pop("car_spots")

        floor = Floor.objects.create(**validated_data)

        cars = [Spot(floor=floor, variety=SpotType.CAR) for _ in range(car_spots)]

        bikes = [
            Spot(floor=floor, variety=SpotType.MOTORCYCLE)
            for _ in range(motorcycle_spots)
        ]

        Spot.objects.bulk_create(cars)
        Spot.objects.bulk_create(bikes)

        return floor
