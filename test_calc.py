import unittest
import calc


class test_calc(unittest.TestCase):
    def setUp(self):
        self.calc = calc.calc()

    def test_sum(self):
        self.assertEqual(self.calc.sum(10,20), 30)

    def test_prod(self):
        self.assertEqual(self.calc.prod(10,20), 200)


if __name__ == "__main__":
    unittest.main()
