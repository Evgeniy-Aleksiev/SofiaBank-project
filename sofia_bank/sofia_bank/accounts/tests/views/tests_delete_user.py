from django.contrib.auth import get_user_model

from sofia_bank.accounts.tests.views.tests_authentication_view import BaseTest

UserModel = get_user_model()


class DeleteUserViewTest(BaseTest):
    def test_get__expect_correct_template_used(self):
        user, profile = self._create_valid_user_and_profile()
        self.client.get(self.get_reversed_url('profile delete', profile.pk))
        self.client.login(**self.VALID_USER_CREDENTIALS)
        self.assertTemplateUsed('accounts/profile_delete.html')

    def test_success_delete_profile_should_redirect(self):
        user, profile = self._create_valid_user_and_profile()
        response = self.client.post(self.get_reversed_url('profile delete', profile.pk))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/accounts/profile/{profile.pk}/delete/')

    def test_deleteUserCancel_should_redirect(self):
        user, profile = self._create_valid_user_and_profile()
        response = self.client.post(self.get_reversed_url('profile delete', profile.pk), data={'cancel': 'cancel'})
        self.assertIsNotNone(profile)
        self.assertEqual(302, response.status_code)



