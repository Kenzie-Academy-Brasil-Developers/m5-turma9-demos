import ipdb
from accounts.models import Account
from rest_framework.test import APITestCase
from rest_framework.views import status


class TestAccountView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = {"username": "user", "password": "1234"}

    def test_register_account_success(self):
        res = self.client.post("/api/register/", data=self.user)
        # ipdb.set_trace()

        # self.assertEqual(res.status_code, 201)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", res.data)
        self.assertIn("date_joined", res.data)

    def test_register_account_missing_keys(self):
        res = self.client.post("/api/register/", data={})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", res.data)
        self.assertIn("username", res.data)

    def test_register_account_with_already_used_username(self):
        self.client.post("/api/register/", data=self.user)
        res = self.client.post("/api/register/", data=self.user)
        # ipdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", res.data)
        self.assertIn("already exists", str(res.data["username"]))
        # Tentar acessar o 'code' do ErrorDetail
        # self.assertIn("already exists", res.json()["username"][0])

    def test_login_sucess(self):
        new_user = Account.objects.create_user(**self.user)

        res = self.client.post("/api/login/", data=self.user)
        # ipdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(new_user.auth_token.key, res.data["token"])

    def test_login_invalid_credentials(self):
        res = self.client.post("/api/login/", data=self.user)
        # ipdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(new_user.auth_token.key, res.data["token"])

    def test_login_missing_fields(self):
        res = self.client.post("/api/login/", data={})
        # ipdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(new_user.auth_token.key, res.data["token"])
        self.assertIn("username", res.data)
        self.assertIn("password", res.data)
