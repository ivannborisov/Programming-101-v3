import unittest

from BankAccount import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.acc_name = "Ivan"
        self.acc_balance = 200
        self.acc_curr = "$"

        self.bank_acc = BankAccount(self.acc_name, self.acc_balance, self.acc_curr)
        self.test_dep_value = 1000
        self.test_str_dun = "Bank account for Ivan with balance of 200$"
        self.test_hist_str = ['Account was created', 'Deposited 1000$', 'Balance check -> 1200$', \
'__int__ check -> 1200$']

    def test_create_new_bank_instance(self):
        self.assertTrue(isinstance(self.bank_acc, BankAccount))

    def test_method_deposit(self):
        new_balance = self.bank_acc.balance() + self.test_dep_value
        self.bank_acc.deposit(self.test_dep_value)

        self.assertEqual(new_balance, self.bank_acc.balance())

    def test_method_balance(self):
        self.assertEqual(self.bank_acc.balance(), self.acc_balance)

    def test_str_dunder(self):
        self.assertEqual(self.test_str_dun, str(self.bank_acc))

    def test_history(self):
        self.bank_acc.deposit(self.test_dep_value)
        self.bank_acc.balance()
        int(self.bank_acc)
        self.assertEqual(self.bank_acc.history(), self.test_hist_str)


if __name__ == '__main__':
    unittest.main()
