from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class ContactViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('main/contacts.html')

    def test_get__expect_correct_context_data(self):
        bank = self.get_atms_and_branches('Branches')
        bank.save()
        bank = self.get_atms_and_branches('ATMs')
        bank.save()
        response = self.client.get(reverse('contacts'))
        self.assertIsNotNone(response.context['banks'])
        self.assertIsNotNone(response.context['atms'])
        bank.delete()