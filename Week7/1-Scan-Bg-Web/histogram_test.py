import unittest

from histogram import Histogram


class HistogramTest(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()
        self.h.add("Apache")
        self.h.add("Apache")

    def test_add(self):
        assert self.h.get_dict().get("Apache") is not None

    def test_count(self):
        self.assertEqual(self.h.count("Apache"), 2)


if __name__ == '__main__':
    unittest.main()
