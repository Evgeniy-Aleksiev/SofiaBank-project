from datetime import datetime, date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from sofia_bank.accounts.models import Profile
from sofia_bank.common_files.helpers import deposit_a_loan
from sofia_bank.main.models import BankLoans, BankSavings, AtmAndBranches, Feedback, ExchangeRates

UserModel = get_user_model()


class BaseTest(django_test.TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.login_url = reverse('login user')
        self.user = {
            'username': 'testuser',
            'password': '12345qew'
        }

    def _create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user
        )

        return user, profile

    def deposit_amount(self, pk):
        loan = self.get_consumer_loan(pk)
        deposit = BankSavings.objects.create(
            types='Deposit',
            amount=1000,
            deposit_date=datetime.now(),
            user_id=pk,
        )
        deposit_a_loan(1000, loan, self.user)
        return loan, deposit

    def get_feedback(self):
        branch = self.get_atms_and_branches('Branches', 7676)
        branch.save()
        return Feedback.objects.create(
            username='Testov',
            details='Test info',
            date=datetime.now(),
            bank_or_atm_number=branch,
        )

    @staticmethod
    def create_exchange_rates():
        return ExchangeRates.objects.create(
            date=datetime.now(),
            currency='EUR',
            fixing=1.9998,
            buy=1.9555,
            sell=1.9444,
            currency_units=1,
        )

    @staticmethod
    def get_atms_and_branches(branch, number):
        return AtmAndBranches.objects.create(
            city='Sofia',
            neighborhood='Nadejda',
            street='Beli Dunav',
            branches_and_atms=branch,
            bank_or_atm_number=str(number),
            open_on_date=datetime.now(),
        )

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

    @staticmethod
    def get_savings(pk):
        return BankSavings.objects.create(
            types='Savings',
            amount=10000,
            deposit_date=datetime.now(),
            user_id=pk,
        )

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
