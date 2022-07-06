from accounts.models import Account
from django.db.utils import IntegrityError
from django.test import TestCase
from parking_lots.models import ParkingLot


# Create your tests here.
class ParkingLotTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.owner = Account.objects.create_user(username="usertest", password="1234")
        cls.name = "Estacionamento Teste"
        cls.parking_lot = ParkingLot(name=cls.name)

    def test_parking_lot_fields(self):
        self.parking_lot.owner = self.owner
        self.parking_lot.save()

        # pl = ParkingLot.objects.get(pk=1)
        # self.assertEqual(pl.name, self.name)

        self.assertEqual(self.parking_lot.name, self.name)
        self.assertIsInstance(self.parking_lot.name, str)
        self.assertIsInstance(self.parking_lot.owner, Account)

    def test_parking_lot_creation_without_owner(self):
        with self.assertRaises(IntegrityError):
            self.parking_lot.save()

    def test_parking_lot_creation_with_owner(self):
        self.parking_lot.owner = self.owner
        self.parking_lot.save()
