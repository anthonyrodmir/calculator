import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(-2, 3), -5)
        self.assertEqual(self.calc.sub(0, 0), 0)
        self.assertEqual(self.calc.sub(3.5, 2.5), 1.0)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(-2, 3), -6)
        self.assertEqual(self.calc.mul(0, 3), 0)
        self.assertEqual(self.calc.mul(2.5, 2), 5.0)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 3), 2)
        self.assertEqual(self.calc.div(-6, 3), -2)
        self.assertEqual(self.calc.div(3.5, 0.5), 7.0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(1, 0)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)
        self.assertEqual(self.calc.pow(-2, 3), -8)
        self.assertEqual(self.calc.pow(2, 0), 1)
        self.assertEqual(self.calc.pow(4, 0.5), 2.0)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2.0)
        self.assertEqual(self.calc.sqrt(0), 0.0)
        self.assertEqual(self.calc.sqrt(2.25), 1.5)
        self.assertEqual(self.calc.sqrt(-100), "10.0i")
