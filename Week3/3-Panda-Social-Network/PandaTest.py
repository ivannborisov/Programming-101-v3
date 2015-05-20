import unittest

from Panda import Panda
from PandaNetwork import PandaNetwork


class PandaTest(unittest.TestCase):

    def setUp(self):
        self.pesho = Panda("Pesho", "pesho@abv.bg", "male")
        self.peshka = Panda("Peshka", "peshka@gmail.com", "female")

    def test_valid_email(self):
        with self.assertRaises(ValueError):
            self.gosho = Panda("asdas", "asdas@abv", "asd")

    def test_create_new_panda_instance(self):
        self.assertTrue(isinstance(self.pesho, Panda))

# __PandaNetwrok________________________________________________________

    def test_add_panda(self):
        net = PandaNetwork()
        net.add_panda(self.pesho)


if __name__ == '__main__':
    unittest.main()
