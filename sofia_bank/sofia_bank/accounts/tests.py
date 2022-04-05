from django.test import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):
    def test_custom_user_model(self):
        self.assertEqual(settings.AUTH_USER_MODEL, "accounts.SofiaBankUser")