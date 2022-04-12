from django.contrib.auth import get_user_model
from django.urls import reverse

from sofia_bank.accounts.models import Profile
from sofia_bank.accounts.tests.views.tests_authentication_view import BaseTest

UserModel = get_user_model()


class DeleteUserVIewTest(BaseTest):
    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user
        )

        return user, profile

    def test_get__expect_correct_template_template_used(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.get(self.get_reversed_url('profile delete', profile.pk))
        self.client.login(**self.VALID_USER_CREDENTIALS)
        self.assertTemplateUsed('accounts/profile_delete.html')

    def test_success_delete_profile_should_redirect(self):
        user, profile = self.__create_valid_user_and_profile()
        response = self.client.post(self.get_reversed_url('profile delete', profile.pk))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/accounts/profile/{profile.pk}/delete/')

    def test_deleteUserCancel_should_redirect(self):
        user, profile = self.__create_valid_user_and_profile()
        # data = self.get_consumer_loan(profile.pk)
        response = self.client.post(self.get_reversed_url('profile delete', profile.pk), data={'cancel': 'cancel'})
        user = UserModel.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(302, response.status_code)


