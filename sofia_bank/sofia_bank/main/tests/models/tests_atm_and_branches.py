from datetime import datetime

from sofia_bank.accounts.tests.base.base_tests import BaseTest
from sofia_bank.main.models import AtmAndBranches


class AtmAndBranchesTest(BaseTest):
    def test_success_create_branches_withStreetAndNeighborhood(self):
        branch = self.get_atms_and_branches()
        self.assertEqual('Branches', branch.branches_and_atms)
        self.assertEqual('Sofia', branch.city)
        self.assertEqual('Nadejda', branch.neighborhood)
        self.assertEqual('Beli Dunav', branch.street)
        self.assertEqual('7676', branch.bank_or_atm_number)
        date_exists = branch.open_on_date is not None
        self.assertTrue(date_exists)
        expected_result = '(7676)| Sofia Nadejda Beli Dunav'
        self.assertEqual(expected_result, str(branch))

    def test_success_create_branches_withoutStreet(self):
        branch = AtmAndBranches(
            city='Sofia',
            neighborhood='Nadejda',
            branches_and_atms='Branches',
            bank_or_atm_number='7676',
            open_on_date=datetime.now(),
        )
        expected_result = '(7676)| Sofia Nadejda '
        self.assertEqual(expected_result, str(branch))

    def test_success_create_branches_withoutNeighborhood(self):
        branch = AtmAndBranches(
            city='Sofia',
            street='Beli Dunav',
            branches_and_atms='Branches',
            bank_or_atm_number='7676',
            open_on_date=datetime.now(),
        )
        expected_result = '(7676)| Sofia  Beli Dunav'
        self.assertEqual(expected_result, str(branch))