from datetime import datetime as dt
from datetime import timedelta, timezone

from django.db import models
from floors.models import SpotType


# Create your models here.
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=10, choices=SpotType.choices)
    arrived_at = models.DateTimeField(auto_now_add=True)
    # nunca usem FLOAT para valor monetario
    # serao armazenados em centavos
    amount_paid = models.IntegerField(null=True, blank=True, default=None)
    paid_at = models.DateTimeField(null=True, blank=True, default=None)
    # amount_paid = models.IntegerField(null=True)
    # paid_at = models.DateTimeField(null=True)

    spot = models.OneToOneField("floors.Spot", on_delete=models.CASCADE, null=True)

    def calculate_payment(self):
        self.paid_at = dt.now(timezone.utc)
        time_elapsed: timedelta = self.paid_at - self.arrived_at
        # import ipdb

        minutes = time_elapsed.total_seconds() // 60

        # 25centavos por minutos
        self.amount_paid = minutes * 25

        self.spot = None

        # ipdb.set_trace()
