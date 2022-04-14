from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class LoanDetailViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        user, _ = self._create_valid_user_and_profile()
        self.client.force_login(user)
        response = self.client.get(self.get_reversed_url('loan detail', user.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('products/loan_details.html')

    def test_create_loanDetail_when_user_not_loggedIn_shouldRedirectToSignIn(self):
        user, _ = self._create_valid_user_and_profile()
        expected_message = f'/accounts/login/?next=/dashboard/loan-detail/{user.pk}/'
        response = self.client.get(self.get_reversed_url('loan detail', user.pk))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_message)

    def test_get_loanDetail_when_user_loggedIn(self):
        user, _ = self._create_valid_user_and_profile()
        self.client.force_login(user)
        loan = self.get_consumer_loan(user.pk)
        self.client.post(reverse('loans'), data={
            'type': loan.type,
            'amount': loan.amount,
            'period': loan.period,
        })
        response = self.client.get(self.get_reversed_url('loan detail', user.pk))
        self.assertIsNotNone(response.context['user_loans'])

