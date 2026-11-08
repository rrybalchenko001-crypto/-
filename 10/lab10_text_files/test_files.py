"""Автоматические проверки чтения матрицы и обработки ошибок."""

import tempfile
import unittest
from pathlib import Path

from files_lab import read_matrix
from main import build_report, read_positive_integer
from table import row_sums, column_sums
from variant import selected_sum


class ReadMatrixTests(unittest.TestCase):
    def read_text(self, content: str):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "matrix.txt"
        path.write_text(content, encoding="utf-8")
        return read_matrix(path)

    def test_valid_matrix(self):
        self.assertEqual(self.read_text("2 3\n1 -2 3\n4 0 -6\n"), [[1, -2, 3], [4, 0, -6]])

    def test_single_element_zero(self):
        self.assertEqual(self.read_text("1 1\n0\n"), [[0]])

    def test_empty_file(self):
        with self.assertRaises(ValueError):
            self.read_text("")

    def test_zero_dimensions(self):
        with self.assertRaises(ValueError):
            self.read_text("0 3\n")

    def test_wrong_number_of_values_in_row(self):
        with self.assertRaisesRegex(ValueError, "[Сс]трока 2"):
            self.read_text("1 2\n7\n")

    def test_extra_data_row(self):
        with self.assertRaises(ValueError):
            self.read_text("1 1\n5\n6\n")

    def test_blank_data_line(self):
        with self.assertRaises(ValueError):
            self.read_text("1 1\n\n")

    def test_non_integer_element(self):
        with self.assertRaises(ValueError):
            self.read_text("1 1\nabc\n")

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                read_matrix(Path(directory) / "missing.txt")


class CalculationsTests(unittest.TestCase):
    def setUp(self):
        self.matrix = [[1, -2, 3], [4, 0, -6]]

    def test_row_sums(self):
        self.assertEqual(row_sums(self.matrix), [2, -2])

    def test_column_sums(self):
        self.assertEqual(column_sums(self.matrix), [5, -2, -3])

    def test_variant_one_positive_elements(self):
        self.assertEqual(selected_sum(self.matrix), 8)

    def test_report(self):
        self.assertEqual(
            build_report(self.matrix),
            "Суммы строк: 2 -2\n"
            "Суммы столбцов: 5 -2 -3\n"
            "Результат варианта 1: 8\n",
        )


if __name__ == "__main__":
    unittest.main()
