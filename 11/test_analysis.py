"""Проверки функций обработки JSON."""

import unittest

from analysis import validate_todos, completed_counts, leaders, select_tasks


SAMPLE = [
    {"id": 1, "userId": 5, "title": "Вода", "completed": True},
    {"id": 2, "userId": 5, "title": "Цикл", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]


class AnalysisTests(unittest.TestCase):
    def test_valid_data(self):
        self.assertEqual(validate_todos(SAMPLE), SAMPLE)

    def test_root_must_be_list(self):
        with self.assertRaises(ValueError):
            validate_todos({})

    def test_id_must_be_positive_integer(self):
        bad = [{"id": True, "userId": 5, "title": "x", "completed": True}]
        with self.assertRaises(ValueError):
            validate_todos(bad)

    def test_title_must_not_be_empty(self):
        bad = [{"id": 1, "userId": 5, "title": " ", "completed": True}]
        with self.assertRaises(ValueError):
            validate_todos(bad)

    def test_completed_must_be_boolean(self):
        bad = [{"id": 1, "userId": 5, "title": "x", "completed": 1}]
        with self.assertRaises(ValueError):
            validate_todos(bad)

    def test_completed_counts(self):
        self.assertEqual(completed_counts(SAMPLE), {5: 2, 10: 2})

    def test_leaders_including_tie(self):
        self.assertEqual(leaders(SAMPLE), [5, 10])

    def test_empty_leaders(self):
        self.assertEqual(leaders([]), [])

    def test_select_user_tasks(self):
        self.assertEqual(len(select_tasks(SAMPLE, 5)), 3)

    def test_unknown_user(self):
        self.assertEqual(select_tasks(SAMPLE, 999), [])


if __name__ == "__main__":
    unittest.main()
