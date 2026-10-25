numbers_text = input("Введите целые числа через пробел: ").strip()

if numbers_text == "":
    numbers = []
else:
    numbers = [int(value) for value in numbers_text.split()]

if not numbers:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = [index for index, value in enumerate(numbers) if value == maximum]

    print("Максимум:", maximum)
    print("Индексы максимума:", positions)
