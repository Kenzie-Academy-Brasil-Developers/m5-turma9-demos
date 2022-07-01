import ipdb
from accounts.models import Account
from floors.models import Floor
from parking_lots.models import ParkingLot
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status


class TestFloorView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.username = "user"
        cls.password = "abc"

        cls.user = Account.objects.create_user(
            username=cls.username, password=cls.password
        )

        cls.token = Token.objects.create(user=cls.user)

        cls.pl1 = ParkingLot.objects.create(name="Parking Lot 1", owner=cls.user)
        cls.pl2 = ParkingLot.objects.create(name="Parking Lot 2", owner=cls.user)

    def test_only_authenticated_users_can_add_floor(self):
        floor_data = {
            "name": "Floor Teste",
            "spot_priority": 2,
            "motorcycle_spots": 1,
            "car_spots": 2,
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        res = self.client.post(
            f"/api/parking-lots/{self.pl1.id}/floors/", data=floor_data
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_only_authenticated_users_can_add_floor_fail(self):
        floor_data = {
            "name": "Floor Teste",
            "spot_priority": 2,
            "motorcycle_spots": 1,
            "car_spots": 2,
        }

        res = self.client.post(
            f"/api/parking-lots/{self.pl1.id}/floors/", data=floor_data
        )

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_list_floors_per_parking_lot(self):
    #     # Criando 5 pisos para o parking lot 1
    #     for i in range(1, 6):
    #         Floor.objects.create(
    #             **{"name": f"Floor {i}", "spot_priority": 2}, parking_lot=self.pl1
    #         )
    #     # Criando 3 pisos para o parking lot 2
    #     for i in range(5, 8):
    #         Floor.objects.create(
    #             **{"name": f"Floor {i}", "spot_priority": 2}, parking_lot=self.pl2
    #         )

    #     # Parking lot 1
    #     res = self.client.get(f"/api/parking-lots/{self.pl1.id}/floors/")
    #     # ipdb.set_trace()
    #     self.assertEqual(len(res.data), 5)
