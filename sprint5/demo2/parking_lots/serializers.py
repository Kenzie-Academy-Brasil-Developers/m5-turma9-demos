from accounts.serializers import AccountSerializer
from rest_framework import serializers

from .models import ParkingLot


class ListParkingLotSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)

    class Meta:
        model = ParkingLot
        # []
        fields = ["id", "name", "owner", "floors"]
        # read_only_fields = ["owner"]
        # depth = 1


class DetailParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = ["id", "name"]
