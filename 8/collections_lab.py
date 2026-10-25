"""Функции лабораторной работы № 8: коллекции и словари."""


def word_counts(text: str) -> dict[str, int]:
    """Считает слова без учёта регистра, удаляя знаки .,!?:; по краям."""
    counts: dict[str, int] = {}
    for raw_word in text.lower().split():
        word = raw_word.strip(".,!?:;")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def common_topics(first: list[str], second: list[str]) -> list[str]:
    """Возвращает общие уникальные темы в алфавитном порядке."""
    return sorted(set(first) & set(second))


def all_topics(first: list[str], second: list[str]) -> list[str]:
    """Возвращает все уникальные темы в алфавитном порядке."""
    return sorted(set(first) | set(second))


def totals_by_category(records: list[dict]) -> dict[str, int]:
    """Возвращает сумму amount для каждой категории."""
    totals: dict[str, int] = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records: list[dict], category: str) -> list[str]:
    """Возвращает названия записей выбранной категории по алфавиту."""
    return sorted(
        record["title"]
        for record in records
        if record["category"] == category
    )


def update_record_amount(record: dict, amount: int) -> dict:
    """Создаёт поверхностную копию записи и меняет amount, не изменяя оригинал."""
    updated = record.copy()
    updated["amount"] = amount
    return updated


# Индивидуальный вариант 8: настольные игры, amount — количество игроков.
records = [
    {"title": "Каркассон", "category": "Стратегические", "amount": 5},
    {"title": "Колонизаторы", "category": "Стратегические", "amount": 4},
    {"title": "Имаджинариум", "category": "Карточные", "amount": 7},
    {"title": "Уно", "category": "Карточные", "amount": 4},
]
