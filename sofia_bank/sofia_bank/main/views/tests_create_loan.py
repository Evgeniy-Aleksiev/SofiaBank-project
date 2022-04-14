from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class CreateLoanViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        user, _ = self._create_valid_user_and_profile()
        self.client.force_login(user)
        response = self.client.get(reverse('loans'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('products/loans.html')

    def test_create_loan_when_user_not_loggedIn_shouldRedirectToSignIn(self):
        expected_message = '/accounts/login/?next=/products-services/loans/'
        response = self.client.get(reverse('loans'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_message)

    def test_get_loan_when_user_loggedIn_shouldAddLoan_and_redirect(self):
        user, _ = self._create_valid_user_and_profile()
        self.client.force_login(user)
        loan = self.get_consumer_loan(user.pk)
        response = self.client.post(reverse('loans'), data={
            'type': loan.type,
            'amount': loan.amount,
            'period': loan.period,
        })
        self.assertRedirects(response, self.get_reversed_url('dashboard', user.pk))
