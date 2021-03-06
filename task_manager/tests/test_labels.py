from django.test import TestCase
from django.test import Client
from django.urls import reverse
from task_manager.labels.models import Label

from .factories import LabelFactory, UserFactory


class LabelCreateChangeDeleteTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.label = LabelFactory.build()
        self.client = Client()
        self.client.force_login(self.user)
        self.client_without_auth = Client()

    def test_create_label(self):
        self.client_without_auth.post(
            reverse("label_create"), {"name": self.label.name}
        )
        self.assertEqual(
            Label.objects.filter(name=self.label.name).exists(),
            False,
        )
        self.client.post(reverse("label_create"), {"name": self.label.name})
        self.assertEqual(
            Label.objects.filter(name=self.label.name).exists(),
            True,
        )

    def test_change_label(self):
        change_label = LabelFactory()
        new_label_name = LabelFactory.build().name
        self.assertNotEqual(change_label.name, new_label_name)
        self.client_without_auth.post(
            reverse("label_chd", kwargs={"pk": change_label.pk}),
            {"name": new_label_name},
        )
        self.assertEqual(
            Label.objects.filter(name=new_label_name).exists(),
            False,
        )
        self.client.post(
            reverse("label_chd", kwargs={"pk": change_label.pk}),
            {"name": new_label_name},
        )
        self.assertEqual(
            Label.objects.filter(name=new_label_name).exists(),
            True,
        )

    def test_delete_label(self):
        delete_label = LabelFactory()
        self.client_without_auth.post(
            reverse("label_del", kwargs={"pk": delete_label.pk})
        )
        self.assertEqual(
            Label.objects.filter(name=delete_label.name).exists(),
            True,
        )
        self.client.post(reverse("label_del", kwargs={"pk": delete_label.pk}))
        self.assertEqual(
            Label.objects.filter(name=delete_label.name).exists(),
            False,
        )
