from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class FeedbackViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('main/feedback.html')

    def test_post_successfully_send_feedback(self):
        feedback = self.get_feedback()
        response = self.client.post(reverse('feedback'), data={
            'username': feedback.username,
            'details': feedback.details,
            'bank_or_atm_number': feedback.bank_or_atm_number,
        })

        self.assertEqual(response.status_code, 200)
