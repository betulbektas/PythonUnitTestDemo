import unittest
import main


class TestCalculator(unittest.TestCase):
    def test_division(self):
        self.assertEqual(main.division(10, 2), 5)
        try:
            self.assertEqual(main.division(5, 0), float('inf'))  # Test for division by zero
        except ZeroDivisionError:
            self.assertTrue(True)
    def test_multiplication(self):
        self.assertEqual(main.multiplication(3, 4), 12)
        self.assertEqual(main.multiplication(0, 7), 0)

    def test_subtraction(self):
        self.assertEqual(main.subtraction(8, 3), 5)
        self.assertEqual(main.subtraction(5, 8), -3)

    def test_addition(self):
        self.assertEqual(main.addition(2, 2), 4)
        self.assertEqual(main.addition(-1, 5), 4)


if __name__ == '__main__':
    unittest.main()