from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class CreateSavingsViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        user, _ = self._create_valid_user_and_profile()
        self.client.force_login(user)
        response = self.client.get(reverse('savings and deposit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('products/savings_and_deposits.html')

    def test_create_savings_when_user_not_loggedIn_shouldRedirectToSignIn(self):
        expected_message = '/accounts/login/?next=/products-services/savings/'
        response = self.client.get(reverse('savings and deposit'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_message)

    def test_get_savings_when_user_loggedIn_shouldAddSavings_and_redirect(self):
        user, _ = self._create_valid_user_and_profile()
        self.client.force_login(user)
        savings = self.get_savings(user.pk)
        response = self.client.post(reverse('savings and deposit'), data={
            'types': savings.types,
            'amount': savings.amount,
        })
        self.assertRedirects(response, self.get_reversed_url('dashboard', user.pk))
