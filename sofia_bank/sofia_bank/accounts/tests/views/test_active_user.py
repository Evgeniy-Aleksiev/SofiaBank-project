from django.contrib import auth
from django.test import TestCase
from django.urls import reverse


class ActivateUserTest(TestCase):
    def setUp(self):
        self.email = 'sofia.bank.project@gmail.com'
        self.username = 'testov'
        self.password = 'asdasd'

    def test_activationSuccess(self):
        self.client.post(reverse('login user'), data={
            'username': self.username,
            'password1': self.password,
        })

        user = auth.get_user(self.client)
        token_regex = r"activate/MQ\/([A-Za-z0-9:\-]+)\/"