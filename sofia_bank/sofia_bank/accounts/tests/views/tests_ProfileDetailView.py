from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from sofia_bank.accounts.models import Profile

UserModel = get_user_model()


class ProfileDetailsViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew'
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'middle_name': 'Testov',
        'last_name': 'Testov',
        'egn': '0000000000',
        'email': 'test@test.bg',
        'mobile_number': '123456789',
        'date_of_birth': date(1999, 4, 13),
    }

    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user
        )

        return user, profile

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 10000000000,
        }))
        self.assertEqual(response.status_code, 404)

    def test_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()

        response = self.client.get(reverse('profile details', kwargs={
            'pk': profile.pk,
        }))
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_dashboard_user_values__expect_is_owner_to_be_true(self):
        user, profile = self.__create_valid_user_and_profile()

        self.client.login(**self.VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('dashboard', kwargs={'pk': profile.pk}))

        self.assertTrue(response.context['total_loans'])
        self.assertTrue(response.context['total_deposits'])
        self.assertTrue(response.context['total_savings'])
        self.assertTrue(response.context['total_loan_paid'])

