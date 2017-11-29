import unittest
from chapter27.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.c = Calculator(5, 3)

    def test_add(self):
        # c = Calculator(5, 3)
        self.assertEqual(8, self.c.add())

    def test_subtract(self):
        # c = Calculator(5, 3)
        self.assertEqual(2, self.c.subtract())

    def tearDown(self):
        del self.c

if __name__ == '__main__':
    unittest.main()