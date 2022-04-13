from sofia_bank.accounts.tests.base.base_tests import BaseTest
from sofia_bank.main.forms import CreateSavingForm


class BankSavingsModelTest(BaseTest):
    def setUp(self) -> None:
        self.user, self.profile = self._create_valid_user_and_profile()

    def test_empty_form(self):
        form = CreateSavingForm(self.user)
        self.assertIn('types', form.fields)
        self.assertIn('amount', form.fields)

    def test_success_post_savings(self):
        savings = self.get_savings(self.user.pk)
        self.assertEqual('Savings', savings.types)
        self.assertEqual(10000, savings.amount)
        date_exists = savings.deposit_date is not None
        self.assertTrue(date_exists)
        self.assertEqual(self.user.pk, savings.user_id)

