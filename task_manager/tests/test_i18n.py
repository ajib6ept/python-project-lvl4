import re

from django.test import Client, TestCase, override_settings
from django.urls import reverse


class InternationalizationLocalizationTest(TestCase):
    def setUp(self):
        self.client = Client()

    @override_settings(LANGUAGE_CODE="en-US", LANGUAGES=(("en", "English"),))
    def test_en_locale(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(
            bool(re.search("[а-яА-Я]", response.content.decode("utf-8"))),
            False,
        )

    @override_settings(LANGUAGE_CODE="ru", LANGUAGES=(("ru", "Russian"),))
    def test_ru_locale(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(
            bool(re.search("[а-яА-Я]", response.content.decode("utf-8"))),
            True,
        )
