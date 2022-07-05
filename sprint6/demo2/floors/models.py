from django.db import models


class Floor(models.Model):
    name = models.CharField(max_length=127)
    spot_priority = models.IntegerField()

    parking_lot = models.ForeignKey(
        "parking_lots.ParkingLot", on_delete=models.CASCADE, related_name="floors"
    )

    def find_spot_for_vehicle_type(self, vehicle_type):
        # Spot.objects.filter(variety=vehicle_type, vehicle=None).first()
        available_spot = self.spots.filter(variety=vehicle_type, vehicle=None).first()

        return available_spot


class SpotType(models.TextChoices):
    CAR = "car"
    MOTORCYCLE = "motorcycle"


class Spot(models.Model):
    variety = models.CharField(
        max_length=127, choices=SpotType.choices, default=SpotType.CAR
    )

    floor = models.ForeignKey(
        "floors.Floor", on_delete=models.CASCADE, related_name="spots"
    )


# Create your models here.
