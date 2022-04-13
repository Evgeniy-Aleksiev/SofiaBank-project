from sofia_bank.accounts.tests.base.base_tests import BaseTest
from sofia_bank.main.forms import FeedbackForm


class FeedbackModelTest(BaseTest):
    def test_empty_form(self):
        form = FeedbackForm(self.user)
        self.assertIn('username', form.fields)
        self.assertIn('details', form.fields)
        self.assertIn('bank_or_atm_number', form.fields)

    def test_get_feedback_by_user(self):
        feedback = self.get_feedback()
        self.assertEqual('Testov', feedback.username)
        self.assertEqual('Test info', feedback.details)
        self.assertEqual('(7676)| Sofia Nadejda Beli Dunav', str(feedback.bank_or_atm_number))
        date_exists = feedback.date is not None
        self.assertTrue(date_exists)
