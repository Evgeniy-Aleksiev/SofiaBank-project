from sofia_bank.accounts.tests.base.base_tests import BaseTest


class UserModelTest(BaseTest):
    def test_regular_user_init(self):
        user, _ = self._create_valid_user_and_profile()
        self.assertEqual('testuser', user.username)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        date_exists = user.date_joined is not None
        self.assertTrue(date_exists)
        self.assertIsNotNone(user.profile)