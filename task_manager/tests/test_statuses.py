from django.test import Client, TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tests.factories import StatusFactory, UserFactory


class StatusCreateChangeDeleteTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.status = StatusFactory.build()
        self.client = Client()
        self.client.force_login(self.user)
        self.client_without_auth = Client()

    def test_create_status(self):
        self.client_without_auth.post(
            reverse("status_create"), {"name": self.status.name}
        )
        self.assertFalse(Status.objects.filter(name=self.status.name).exists())
        self.client.post(reverse("status_create"), {"name": self.status.name})
        self.assertTrue(Status.objects.filter(name=self.status.name).exists())

    def test_change_status(self):
        change_status = StatusFactory()
        new_status_name = StatusFactory.build().name
        self.assertNotEqual(change_status.name, new_status_name)
        self.client_without_auth.post(
            reverse("status_chd", kwargs={"pk": change_status.pk}),
            {"name": new_status_name},
        )
        self.assertFalse(Status.objects.filter(name=new_status_name).exists())
        self.client.post(
            reverse("status_chd", kwargs={"pk": change_status.pk}),
            {"name": new_status_name},
        )
        self.assertTrue(Status.objects.filter(name=new_status_name).exists())

    def test_delete_status(self):
        delete_status = StatusFactory()
        self.client_without_auth.post(
            reverse("status_del", kwargs={"pk": delete_status.pk})
        )
        self.assertTrue(
            Status.objects.filter(name=delete_status.name).exists()
        )
        self.client.post(
            reverse("status_del", kwargs={"pk": delete_status.pk})
        )
        self.assertFalse(
            Status.objects.filter(name=delete_status.name).exists()
        )
