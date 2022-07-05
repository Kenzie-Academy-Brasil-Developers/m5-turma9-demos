from django.db import models


# Create your models here.
class ParkingLot(models.Model):
    name = models.CharField(max_length=127)

    owner = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="parking_lots"
    )
