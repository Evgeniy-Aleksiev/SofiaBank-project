from datetime import datetime, date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from sofia_bank.accounts.models import Profile
from sofia_bank.main.models import BankLoans

UserModel = get_user_model()


class BaseTest(django_test.TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.login_url = reverse('login user')
        self.user = {
            'username': 'testuser',
            'password': '12345qew'
        }

    @staticmethod
    def get_reversed_url(url, pk=None):
        if pk is not None:
            return reverse(url,  kwargs={'pk': pk, })
        return reverse(url)

    @staticmethod
    def get_consumer_loan(pk):
        return BankLoans.objects.create(
            type='Consumer Loans',
            amount=10000,
            period=10,
            loan_date=datetime.now(),
            user_id=pk,
        )

    def _create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user
        )

        return user, profile

    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew'
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Testov',
        'middle_name': 'Testov',
        'last_name': 'Testov',
        'egn': '0000000000',
        'email': 'test@test.bg',
        'mobile_number': '123456789',
        'date_of_birth': date(1999, 4, 13),
    }
