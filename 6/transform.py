numbers_text = input("Введите целые числа через пробел: ").strip()

if numbers_text == "":
    numbers = []
else:
    numbers = [int(value) for value in numbers_text.split()]

# Создаём новый список: отрицательные числа заменяем их модулем.
transformed = [abs(number) if number < 0 else number for number in numbers]

print("Исходный список:", numbers)
print("Новый список:", transformed)
