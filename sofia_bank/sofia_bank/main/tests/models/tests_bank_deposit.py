from sofia_bank.accounts.tests.base.base_tests import BaseTest


class BankDepositModelTest(BaseTest):
    def setUp(self) -> None:
        self.user, self.profile = self._create_valid_user_and_profile()

    def test_success_post_deposit(self):
        loan, deposit = self.deposit_amount(self.user.pk)
        self.assertEqual('Deposit', deposit.types)
        self.assertEqual(1000, deposit.amount)
        date_exists = deposit.deposit_date is not None
        self.assertTrue(date_exists)
        self.assertEqual(self.user.pk, deposit.user_id)
        self.assertEqual(9000, loan.amount)
        self.assertEqual(deposit.user_id, loan.user_id)

