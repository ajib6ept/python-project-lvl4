from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


class UserCreateChangeDeleteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = {
            "username": "test_username",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "password1": "Qw1234566",
            "password2": "Qw1234566",
        }

    def create_test_user(self):
        return self.client.post(reverse("register"), self.data)

    def test_create_user(self):
        response = self.create_test_user()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            User.objects.filter(username=self.data["username"]).exists(), True
        )

    def test_change_user(self):
        self.create_test_user()
        test_user_pk = User.objects.get(username=self.data["username"]).pk
        new_data = self.data.copy()
        new_data["username"] = new_data["username"] + "1"
        self.client.post(
            reverse("user_chg", kwargs={"pk": test_user_pk}), new_data
        )
        self.assertEqual(
            User.objects.filter(username=self.data["username"]).exists(), True
        )
        self.client.login(
            username=self.data["username"], password=self.data["password1"]
        )
        self.client.post(
            reverse("user_chg", kwargs={"pk": test_user_pk}), new_data
        )
        self.assertEqual(
            User.objects.filter(username=self.data["username"]).exists(), False
        )

    def test_delete_user(self):
        self.create_test_user()
        test_user_pk = User.objects.get(username=self.data["username"]).pk
        self.client.post(reverse("user_del", kwargs={"pk": test_user_pk}))
        self.assertEqual(
            User.objects.filter(username=self.data["username"]).exists(), True
        )
        self.client.login(
            username=self.data["username"], password=self.data["password1"]
        )
        self.client.post(reverse("user_del", kwargs={"pk": test_user_pk}))
        self.assertEqual(
            User.objects.filter(username=self.data["username"]).exists(), False
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
