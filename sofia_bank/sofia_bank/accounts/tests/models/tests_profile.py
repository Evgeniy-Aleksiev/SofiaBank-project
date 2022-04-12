from datetime import date

from django import test as django_test
from django.core.exceptions import ValidationError

from sofia_bank.accounts.models import Profile


class ProfileTests(django_test.TestCase):
    VALID_USER_DATA = {
        'first_name': 'Test',
        'middle_name': 'Testov',
        'last_name': 'Testov',
        'egn': '0000000000',
        'email': 'test@test.bg',
        'mobile_number': '123456789',
        'date_of_birth': date(1999, 4, 13),
        'gender': 'Male',
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_USER_DATA)
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
        profile = Profile(**self.VALID_USER_DATA)

        self.assertEqual('Test Testov Testov', profile.full_name)