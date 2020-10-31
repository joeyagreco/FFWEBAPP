import unittest

from packages.Calculator.Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add_two_positive_numbers(self):
        calculator = Calculator()
        self.assertEqual(3, calculator.add(1, 2))

    def test_add_one_positive_number(self):
        calculator = Calculator()
        self.assertEqual(-1, calculator.add(1, -2))

    def test_add_two_negative_numbers(self):
        calculator = Calculator()
        self.assertEqual(-3, calculator.add(-1, -2))




