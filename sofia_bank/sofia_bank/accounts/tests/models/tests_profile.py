from datetime import date

from django import test as django_test
from django.core.exceptions import ValidationError

from sofia_bank.accounts.models import Profile
from sofia_bank.accounts.tests.base.base_tests import BaseTest


class ProfileTests(BaseTest):
    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        user, profile = self._create_valid_user_and_profile()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit_or_symbol__expect_fail(self):
        first_name = 'Test1'
        profile = Profile(first_name=first_name,)
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        user, profile = self._create_valid_user_and_profile()
        self.assertEqual('Testov Testov Testov', profile.full_name)