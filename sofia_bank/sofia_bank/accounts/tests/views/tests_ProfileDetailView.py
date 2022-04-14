from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest

UserModel = get_user_model()


class ProfileDetailsViewTests(BaseTest):
    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(self.get_reversed_url('profile details', 3))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('main/404.html')

    def test_correct_template(self):
        user, profile = self._create_valid_user_and_profile()

        self.client.get(reverse('profile details', kwargs={'pk': profile.pk,}))
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_dashboard_user_values__expect_is_owner_to_be_true(self):
        user, profile = self._create_valid_user_and_profile()

        self.client.login(**self.VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('dashboard', kwargs={'pk': profile.pk}))

        self.assertTrue(response.context['total_loans'])
        self.assertTrue(response.context['total_deposits'])
        self.assertTrue(response.context['total_savings'])
        self.assertTrue(response.context['total_loan_paid'])


class ProfileEditViewTest(BaseTest):
    PROFILE_NEW_DATA = {
        'first_name': 'Testov',
        'middle_name': 'Testov',
        'last_name': 'Testov',
        'egn': '0000000000',
        'email': 'test@test.bg',
        'mobile_number': '987654321',
        'date_of_birth': date(1999, 4, 13),
    }

    def test_get__expect_correct_template_used(self):
        user, profile = self._create_valid_user_and_profile()
        self.client.get(self.get_reversed_url('profile edit', profile.pk))
        self.client.login(**self.VALID_USER_CREDENTIALS)
        self.assertTemplateUsed('accounts/profile_edit.html')

    def test_get__expect_correct_context(self):
        user, profile = self._create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)
        response = self.client.post(self.get_reversed_url('profile edit', profile.pk), data=self.PROFILE_NEW_DATA)
        self.assertEqual(response.status_code, 302)
        profile.refresh_from_db()
        self.assertEqual('987654321', profile.mobile_number)

