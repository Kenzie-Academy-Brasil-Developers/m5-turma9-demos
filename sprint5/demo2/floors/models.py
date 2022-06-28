from django.db import models


# Create your models here.
class Floor(models.Model):
    name = models.CharField(max_length=127)
    spot_priority = models.IntegerField()

    parking_lot = models.ForeignKey(
        "parking_lots.ParkingLot", on_delete=models.CASCADE, related_name="floors"
    )
