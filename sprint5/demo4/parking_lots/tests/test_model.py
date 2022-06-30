from accounts.models import Account
from django.db.utils import IntegrityError
from django.test import TestCase
from parking_lots.models import ParkingLot


# Create your tests here.
class ParkingLotTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print()
        print("Executando setUpData")

        cls.owner = Account.objects.create_user(username="usertest", password="1234")
        cls.parking_lot = ParkingLot(name="Estacionamento Teste")

    @classmethod
    def setUp(cls) -> None:
        print("Executando setUp")
        # print(cls.parking_lot.owner)

    def test_parking_lot_creation_without_owner(self):
        print("Executando test_parking_lot_creation_without_owner")
        # print(self.parking_lot.owner)
        # with self.assertRaises(IntegrityError)
        with self.assertRaises(IntegrityError):
            self.parking_lot.save()

    def test_parking_lot_creation_with_owner(self):
        self.parking_lot.owner = self.owner
        self.parking_lot.save()
        print(self.parking_lot.owner)
