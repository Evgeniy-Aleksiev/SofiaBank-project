from sofia_bank.accounts.tests.base.base_tests import BaseTest
from sofia_bank.main.forms import CreateLoanForm


class BankLoansModelTest(BaseTest):
    def setUp(self) -> None:
        self.user, self.profile = self._create_valid_user_and_profile()

    def test_empty_form(self):
        form = CreateLoanForm(self.user)
        self.assertIn('type', form.fields)
        self.assertIn('amount', form.fields)
        self.assertIn('period', form.fields)

    def test_success_post_consumer_loan(self):
        loan = self.get_consumer_loan(self.user.pk)
        self.assertEqual('Consumer Loans', loan.type)
        self.assertEqual(10000, loan.amount)
        self.assertEqual(10, loan.period)
        date_exists = loan.loan_date is not None
        self.assertTrue(date_exists)
        self.assertEqual(self.user.pk, loan.user_id)
