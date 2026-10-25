"""Автоматические проверки функций из functions.py."""

import unittest
from functions import sum_digits, average, normalize_text


class TestFunctions(unittest.TestCase):
    def test_sum_digits_positive(self):
        self.assertEqual(sum_digits(12345), 15)

    def test_sum_digits_negative(self):
        self.assertEqual(sum_digits(-907), 16)

    def test_sum_digits_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_average_regular_list(self):
        self.assertEqual(average([2, 4, 6]), 4)

    def test_average_empty_list(self):
        self.assertIsNone(average([]))

    def test_average_does_not_change_list(self):
        values = [1, 2, 3]
        original = values.copy()
        average(values)
        self.assertEqual(values, original)

    def test_normalize_text(self):
        self.assertEqual(
            normalize_text("  ПРИВЕТ   Мир  \n Python "),
            "привет мир python",
        )

    def test_normalize_empty_text(self):
        self.assertEqual(normalize_text("   \n  "), "")


if __name__ == "__main__":
    unittest.main()
