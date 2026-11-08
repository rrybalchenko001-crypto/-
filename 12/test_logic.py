
"""Автоматические тесты основных функций проекта."""

import unittest

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)


class RouteManagerTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {
                "id": 1,
                "title": "Основная задача",
                "category": "Пеший",
                "amount": 4,
                "completed": False,
            },
            {
                "id": 2,
                "title": "Дополнительная задача",
                "category": "Горный",
                "amount": 2,
                "completed": True,
            },
        ]

    def test_add_record(self):
        record = add_record(self.records, "Лесной маршрут", "Пеший", 8)
        self.assertEqual(record["id"], 3)
        self.assertFalse(record["completed"])

    def test_search_is_case_insensitive(self):
        self.assertEqual(len(find_records(self.records, "ПЕШИЙ")), 1)

    def test_change_status(self):
        set_completed(self.records, 1, True)
        self.assertTrue(self.records[0]["completed"])

    def test_delete_does_not_reuse_id(self):
        delete_record(self.records, 1)
        new_record = add_record(self.records, "Новый маршрут", "Велосипедный", 5)
        self.assertEqual(new_record["id"], 3)

    def test_statistics(self):
        result = statistics(self.records)
        self.assertEqual(result["total"], 2)
        self.assertEqual(result["completed"], 1)
        self.assertEqual(result["not_completed"], 1)
        self.assertEqual(result["total_amount"], 6.0)

    def test_duplicate_id_is_rejected(self):
        broken = self.records + [dict(self.records[0])]
        with self.assertRaises(ValueError):
            validate_records(broken)

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            add_record(self.records, "  ", "Пеший", 3)

    def test_missing_id_is_reported(self):
        with self.assertRaises(ValueError):
            set_completed(self.records, 99, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
