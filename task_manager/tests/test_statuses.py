from django.test import TestCase
from django.test import Client
from django.urls import reverse
from ..models import Status


class StatusCreateChangeDeleteTest(TestCase):
    def setUp(self):
        self.data = {
            "username": "test_username",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "password1": "Qw1234566",
            "password2": "Qw1234566",
            "status_name": "test_status_name",
        }
        self.test_status_name = "test_status_name"
        self.client = Client()
        self.client.post(reverse("register"), self.data)
        self.client.login(
            username=self.data["username"], password=self.data["password1"]
        )
        self.client_without_auth = Client()

    def create_test_status(self, name="test_status_name"):
        return self.client.post(reverse("status_create"), {"name": name})

    def test_create_status(self):
        self.client_without_auth.post(
            reverse("status_create"), {"name": self.data["status_name"]}
        )
        self.assertEqual(
            Status.objects.filter(name=self.data["status_name"]).exists(),
            False,
        )
        self.client.post(
            reverse("status_create"), {"name": self.data["status_name"]}
        )
        self.assertEqual(
            Status.objects.filter(name=self.data["status_name"]).exists(),
            True,
        )

    def test_change_status(self):
        self.create_test_status()
        test_status_pk = Status.objects.get(name=self.data["status_name"]).pk
        new_data = self.data.copy()
        new_data["status_name"] = new_data["status_name"] + "1"
        self.client_without_auth.post(
            reverse("status_chd", kwargs={"pk": test_status_pk}),
            {"name": new_data["status_name"]},
        )
        self.assertEqual(
            Status.objects.filter(name=new_data["status_name"]).exists(),
            False,
        )
        self.client.post(
            reverse("status_chd", kwargs={"pk": test_status_pk}),
            {"name": new_data["status_name"]},
        )
        self.assertEqual(
            Status.objects.filter(name=new_data["status_name"]).exists(),
            True,
        )

    def test_delete_status(self):
        self.create_test_status()
        test_status_pk = Status.objects.get(name=self.data["status_name"]).pk
        self.client_without_auth.post(
            reverse("status_del", kwargs={"pk": test_status_pk}),
            {"name": self.data["status_name"]},
        )
        self.assertEqual(
            Status.objects.filter(name=self.data["status_name"]).exists(),
            True,
        )
        self.client.post(
            reverse("status_del", kwargs={"pk": test_status_pk}),
            {"name": self.data["status_name"]},
        )
        self.assertEqual(
            Status.objects.filter(name=self.data["status_name"]).exists(),
            False,
        )
