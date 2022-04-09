from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .factories import UserFactory
from task_manager.users.models import TaskUser


class UserCreateChangeDeleteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_user = UserFactory.build()

    def from_user_factory_item_to_dict(self, item):
        return {
            "first_name": item.first_name,
            "last_name": item.last_name,
            "username": item.username,
            "password1": item.password,
            "password2": item.password,
        }

    def test_create_user(self):
        self.assertEqual(
            TaskUser.objects.filter(username=self.new_user.username).exists(),
            False,
        )
        new_user_dict = self.from_user_factory_item_to_dict(self.new_user)
        response = self.client.post(reverse("register"), new_user_dict)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            TaskUser.objects.filter(username=self.new_user.username).exists(),
            True,
        )

    def test_change_user(self):
        change_user = UserFactory()
        change_user_dict = self.from_user_factory_item_to_dict(change_user)
        new_username = UserFactory.build().username
        self.assertNotEqual(change_user.username, new_username)
        change_user_dict["username"] = new_username
        self.client.post(
            reverse("user_chg", kwargs={"pk": change_user.pk}),
            change_user_dict,
        )
        self.assertEqual(
            TaskUser.objects.filter(username=change_user.username).exists(),
            True,
        )
        self.client.force_login(change_user)
        self.client.post(
            reverse("user_chg", kwargs={"pk": change_user.pk}),
            change_user_dict,
        )
        self.assertEqual(
            TaskUser.objects.filter(username=change_user.username).exists(),
            False,
        )

    def test_delete_user(self):
        delete_user = UserFactory()
        self.client.post(reverse("user_del", kwargs={"pk": delete_user.pk}))
        self.assertEqual(
            TaskUser.objects.filter(username=delete_user.username).exists(),
            True,
        )
        self.client.force_login(delete_user)
        self.client.post(reverse("user_del", kwargs={"pk": delete_user.pk}))
        self.assertEqual(
            TaskUser.objects.filter(username=delete_user.username).exists(),
            False,
        )


# other file


# class TaskManageMessagesTest(TestCase):
#     def test_success_messgate(self):
#         pass

#     def test_failure_message(self):
#         pass


# class TaskManagerOtherTests(TestCase):
#     def test_form_validation(self):
#         pass

#     def test_locale(self):
#         pass
