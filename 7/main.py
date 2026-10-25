"""Точка входа: ввод данных и демонстрация функций из functions.py."""

from functions import sum_digits, average, normalize_text


def main() -> None:
    try:
        number = int(input("Введите целое число: "))
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        return

    numbers_input = input(
        "Введите числа через пробел (оставьте строку пустой для пустого списка): "
    ).strip()

    try:
        numbers = [float(value) for value in numbers_input.split()] if numbers_input else []
    except ValueError:
        print("Ошибка: список должен содержать только числа.")
        return

    text = input("Введите произвольный текст: ")

    print("Сумма цифр:", sum_digits(number))
    result = average(numbers)
    if result is None:
        print("Среднее:", "Нет данных")
    else:
        print("Среднее:", result)
    print("Нормализованный текст:", normalize_text(text))


if __name__ == "__main__":
    main()
