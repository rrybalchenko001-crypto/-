"""Функции для лабораторной работы № 7."""


def sum_digits(number: int) -> int:
    """Возвращает сумму цифр целого числа, взятого по модулю."""
    number = abs(number)
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total


def average(numbers: list[float]) -> float | None:
    """Возвращает среднее арифметическое списка или None для пустого списка."""
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def normalize_text(text: str) -> str:
    """Переводит текст в нижний регистр и нормализует пробелы."""
    return " ".join(text.lower().split())
