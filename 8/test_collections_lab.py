"""Проверки обязательных заданий и индивидуального варианта 8."""

import unittest
from collections_lab import (
    records,
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    update_record_amount,
)


class TestWordCounts(unittest.TestCase):
    def test_word_counts_example(self):
        self.assertEqual(word_counts("Python, python! SQL"), {"python": 2, "sql": 1})

    def test_empty_text(self):
        self.assertEqual(word_counts(""), {})


class TestTopics(unittest.TestCase):
    def test_common_topics(self):
        self.assertEqual(
            common_topics(["Python", "SQL", "Python"], ["SQL", "Git"]),
            ["SQL"],
        )

    def test_all_topics(self):
        self.assertEqual(
            all_topics(["Python", "SQL"], ["SQL", "Git"]),
            ["Git", "Python", "SQL"],
        )

    def test_input_list_order_is_not_changed(self):
        first = ["SQL", "Python", "SQL"]
        original = first.copy()
        common_topics(first, ["SQL"])
        self.assertEqual(first, original)


class TestRecords(unittest.TestCase):
    def test_totals_by_category(self):
        self.assertEqual(
            totals_by_category(records),
            {"Стратегические": 9, "Карточные": 11},
        )

    def test_titles_sorted(self):
        self.assertEqual(
            titles_in_category(records, "Стратегические"),
            ["Каркассон", "Колонизаторы"],
        )

    def test_unknown_category_returns_empty_list(self):
        self.assertEqual(titles_in_category(records, "Неизвестная категория"), [])

    def test_shallow_copy_and_update(self):
        original = records[0]
        original_before = original.copy()
        updated = update_record_amount(original, 6)
        self.assertEqual(updated["amount"], 6)
        self.assertEqual(original, original_before)
        self.assertIsNot(updated, original)


if __name__ == "__main__":
    unittest.main()
