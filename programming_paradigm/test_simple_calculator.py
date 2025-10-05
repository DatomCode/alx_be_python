import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
# """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        # """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        # """Test the addition method with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 10), 10)

    def test_subtraction(self):
        # """Test the subtraction method with positive, negative, and zero values."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-2, -2), 0)
        self.assertEqual(self.calc.subtract(0, 7), -7)

    def test_multiplication(self):
        # """Test the multiplication method with positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_division(self):
        # """Test the division method including division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(7, -7), -1)
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Edge case: division by zero
        self.assertIsNone(self.calc.divide(5, 0))


if __name__ == "__main__":
    unittest.main()
