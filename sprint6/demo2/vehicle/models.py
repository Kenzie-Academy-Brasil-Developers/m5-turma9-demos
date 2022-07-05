from django.db import models
from floors.models import SpotType


# Create your models here.
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=10, choices=SpotType.choices)
    arrived_at = models.DateTimeField(auto_now_add=True)
    # nunca usem FLOAT para valor monetario
    amount_paid = models.IntegerField(null=True, blank=True, default=None)
    paid_at = models.DateTimeField(null=True, blank=True, default=None)
    # amount_paid = models.IntegerField(null=True)
    # paid_at = models.DateTimeField(null=True)

    spot = models.OneToOneField("floors.Spot", on_delete=models.CASCADE, null=True)
