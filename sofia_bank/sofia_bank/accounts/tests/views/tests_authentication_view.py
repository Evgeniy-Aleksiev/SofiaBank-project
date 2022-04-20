from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse

from sofia_bank.accounts.forms import CreateProfileForm
from sofia_bank.accounts.tests.base.base_tests import BaseTest
from sofia_bank.main.models import UserModel


class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('account/profile_create.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user)
        self.assertEqual(response.status_code, 200)

    def test_signUp_whenWrongPassword2_shouldReturnFormInvalid(self):
        response = self.client.post(self.register_url, data={
            'username': UserModel.username,
            'password1': UserModel.password,
            'password2': 'wrong pass2',
        })
        is_valid = response.context_data['form'].is_valid()
        self.assertFalse(is_valid)
        errors = response.context_data['form'].errors['password2']
        self.assertIn('The two password fields didn’t match.', errors)


class SignInViewTests(BaseTest):
    def test_get__expect_correct_template_used(self):
        response = self.client.get(reverse('login user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login_page.html")

    def test_post__when_user_logged_in__expect_redirect(self):
        self.client.post(self.register_url, self.user, format='accounts/login_page.html')
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        user.is_active = True
        user.save()
        response = self.client.post(reverse('login user'), self.user, format='accounts/login_page.html')
        self.assertEqual(response.status_code, 302)

    def test_get__when_user_successfully_log_in(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        user.save()
        self.client.login(**self.VALID_USER_CREDENTIALS)
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        user.delete()


class SignOutViewTest(BaseTest):
    def test_signOut_success_should_redirect(self):
        self._create_valid_user_and_profile()
        is_logged_in = self.client.login(username='testuser', password='12345qew')
        self.assertTrue(is_logged_in)
        self.client.logout()
        response = self.client.get(reverse('logout user'))
        self.assertEqual(response.status_code, 302)
