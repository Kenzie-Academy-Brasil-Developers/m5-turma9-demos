from datetime import datetime

from accounts.models import Account
from django.core.exceptions import ValidationError
from django.test import TestCase
from floors.models import Floor, Spot
from parking_lots.models import ParkingLot
from vehicles.models import Vehicle


# Create your tests here.
class VehicleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = Account.objects.create_user(username="user", password="pass123")
        pl = ParkingLot.objects.create(name="Parking Lot 1", owner=user)
        floor = Floor.objects.create(name="Floor 1", spot_priority=1, parking_lot=pl)

        cls.car_spot = Spot.objects.create(variety="car", floor=floor)
        cls.motorcycle_spot = Spot.objects.create(variety="motorcycle", floor=floor)

        cls.car_data = {"license_plate": "AAA-1234", "vehicle_type": "car"}
        cls.car = Vehicle(**cls.car_data)

    def test_car_fields(self):
        self.car.save()

        self.assertEqual(self.car.license_plate, self.car_data["license_plate"])
        self.assertEqual(self.car.vehicle_type, self.car_data["vehicle_type"])
        self.assertIsNone(self.car.paid_at)
        self.assertIsNone(self.car.amount_paid)
        self.assertIsNone(self.car.spot)
        self.assertIsInstance(self.car.arrived_at, datetime)

    def test_car_relationship_with_car_spot(self):
        import ipdb

        self.car.spot = self.car_spot

        self.car.save()

        # ipdb.set_trace()
        self.assertIs(self.car.spot, self.car_spot)
        self.assertIs(self.car_spot.vehicle, self.car)

    def test_car_wrong_spot(self):
        import ipdb

        self.car.spot = self.car_spot
        self.car.vehicle_type = "tico tico"

        with self.assertRaises(ValidationError):
            self.car.full_clean()

        # self.car.save()

        ipdb.set_trace()
