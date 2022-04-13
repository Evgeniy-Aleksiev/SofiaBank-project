from django.contrib.auth import get_user_model
from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest

UserModel = get_user_model()


class ProfileDetailsViewTests(BaseTest):
    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get('something/really/weird/')
        self.assertEqual(response.status_code, 404)

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

