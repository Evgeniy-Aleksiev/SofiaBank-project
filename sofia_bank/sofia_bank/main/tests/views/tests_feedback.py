from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class FeedbackViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('main/feedback.html')