from datetime import date

from django import test as django_test
from django.urls import reverse

from sofia_bank.accounts.models import Profile
from sofia_bank.main.models import UserModel


class BaseTest(django_test.TestCase):
    def setUp(self) -> None:
        self.register_url=reverse('register')
        self.login_url=reverse('login user')
        self.user = {
            'username': 'testuser',
            'password': '12345qew'
        }

    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew'
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Testov',
        'middle_name': 'Testov',
        'last_name': 'Testov',
        'egn': '0000000000',
        'email': 'test@test.bg',
        'mobile_number': '123456789',
        'date_of_birth': date(1999, 4, 13),
    }


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


