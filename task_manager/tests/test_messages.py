import re

from django.test import Client, TestCase, override_settings
from django.urls import reverse

from .factories import UserFactory

SUCCESS_CLASS_NAME = "alert alert-success alert-dismissible fade show"
FAILURE_CLASS_NAME = "alert alert-danger alert-dismissible fade show"


class TaskMessagesTest(TestCase):
    def setUp(self):
        self.new_user = UserFactory.build()
        self._create_user(self.new_user)
        self.client = Client()

    def _create_user(self, new_user):
        new_user_dict = {
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "username": new_user.username,
            "password1": new_user.password,
            "password2": new_user.password,
        }
        self.client.post(reverse("register"), new_user_dict)

    @override_settings(LANGUAGE_CODE="ru", LANGUAGES=(("ru", "Russian"),))
    def test_success_ru_message(self):
        response = self.client.post(
            reverse("user_login"),
            {
                "username": self.new_user.username,
                "password": self.new_user.password,
            },
            follow=True,
        )
        html_response = response.content.decode("utf-8")
        self.assertTrue(SUCCESS_CLASS_NAME in html_response)
        html_code_message = re.findall(
            rf'<div class="{SUCCESS_CLASS_NAME}"(.*?)<\/div>',
            html_response,
            flags=re.S,
        )[0]
        self.assertTrue(bool(re.search("[а-яА-Я]", html_code_message)))

    @override_settings(LANGUAGE_CODE="en-US", LANGUAGES=(("en", "English"),))
    def test_success_en_message(self):
        response = self.client.post(
            reverse("user_login"),
            {
                "username": self.new_user.username,
                "password": self.new_user.password,
            },
            follow=True,
        )
        html_response = response.content.decode("utf-8")
        self.assertTrue(SUCCESS_CLASS_NAME in html_response)
        html_code_message = re.findall(
            rf'<div class="{SUCCESS_CLASS_NAME}"(.*?)<\/div>',
            html_response,
            flags=re.S,
        )[0]
        self.assertFalse(bool(re.search("[а-яА-Я]", html_code_message)))

    @override_settings(LANGUAGE_CODE="ru", LANGUAGES=(("ru", "Russian"),))
    def test_failure_ru_message(self):
        response = self.client.post(
            reverse("user_login"),
            {
                "username": "1",
                "password": "1",
            },
            follow=True,
        )
        html_response = response.content.decode("utf-8")
        self.assertTrue(FAILURE_CLASS_NAME in html_response)
        html_code_message = re.findall(
            rf'<div class="{FAILURE_CLASS_NAME}"(.*?)<\/div>',
            html_response,
            flags=re.S,
        )[0]
        self.assertTrue(bool(re.search("[а-яА-Я]", html_code_message)))

    @override_settings(LANGUAGE_CODE="en-US", LANGUAGES=(("en", "English"),))
    def test_failure_en_message(self):
        response = self.client.post(
            reverse("user_login"),
            {
                "username": "1",
                "password": "1",
            },
            follow=True,
        )
        html_response = response.content.decode("utf-8")
        self.assertTrue(FAILURE_CLASS_NAME in html_response)
        html_code_message = re.findall(
            rf'<div class="{FAILURE_CLASS_NAME}"(.*?)<\/div>',
            html_response,
            flags=re.S,
        )[0]
        self.assertFalse(bool(re.search("[а-яА-Я]", html_code_message)))
