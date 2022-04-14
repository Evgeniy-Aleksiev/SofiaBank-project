from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class HomeViewTests(BaseTest):
    def test_get__expect_correct_template_used(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("main/home_page.html")

    def test_get_correct_exchange_rates_date(self):
        exchange_rates = self.create_exchange_rates()
        exchange_rates.save()
        response = self.client.get(reverse('index'))
        self.assertTrue(response.context.get('exchanges'))
        self.assertTrue('EUR' in exchange_rates.currency)
        exchange_rates.delete()
