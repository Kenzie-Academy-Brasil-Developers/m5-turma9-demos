from accounts.serializers import AccountSerializer
from floors.serializers import FloorSerializer
from rest_framework import serializers

from .models import ParkingLot


class ListParkingLotSerializer(serializers.ModelSerializer):
    """
    Lista informações gerais sobre o estacionamento
    ```
    {
        "id": 1,
        "name": "Estacionamento Hot Wheels",
        "floor_count": 4,
        "owner": 1
    }
    ```
    """

    class Meta:
        model = ParkingLot
        fields = ["id", "name", "floor_count", "owner"]

    # floor_count = serializers.SerializerMethodField("random_floor_count")
    floor_count = serializers.SerializerMethodField()

    # def random_floor_count(self, parking_lot: ParkingLot):
    #     """SELECT * FROM TABLE_FLOOR where parking_lot_id=1;"""
    #     return parking_lot.floors.count()

    def get_floor_count(self, parking_lot: ParkingLot) -> int:
        """SELECT COUNT(*) FROM TABLE_FLOOR where parking_lot_id=1;"""
        return parking_lot.floors.count()


class DetailParkingLotSerializer(serializers.ModelSerializer):
    """
    Lista informações detalhadas sobre o estacionamento
    ```
    {
        "id": 1,
        "name": "Estacionamento Hot Wheels",
        "floors": [
            {
                "id": 1,
                "name": "floor 3",
                "spot_priority": 2
            }
        ],
        "owner": {
            "id": 1,
            "username": "chrystian",
            "is_superuser": true,
            "is_staff": true,
            "date_joined": "2022-06-28T12:33:11.529660Z"
        }
    }
    ```
    """

    owner = AccountSerializer(read_only=True)
    floors = FloorSerializer(many=True, read_only=True)

    class Meta:
        model = ParkingLot
        fields = ["id", "name", "floors", "owner"]
