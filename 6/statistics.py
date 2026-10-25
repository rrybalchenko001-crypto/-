numbers_text = input("Введите целые числа через пробел: ").strip()

if numbers_text == "":
    print("Нет данных")
else:
    numbers = [int(value) for value in numbers_text.split()]

    print("Количество:", len(numbers))
    print("Сумма:", sum(numbers))
    print("Минимум:", min(numbers))
    print("Максимум:", max(numbers))
    print(f"Среднее: {sum(numbers) / len(numbers):.2f}")
