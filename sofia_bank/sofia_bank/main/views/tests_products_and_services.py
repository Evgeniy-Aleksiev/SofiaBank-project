from django.urls import reverse

from sofia_bank.accounts.tests.base.base_tests import BaseTest


class ProductsAndServicesViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        response = self.client.get(reverse('products and services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('main/products_and_services.html')