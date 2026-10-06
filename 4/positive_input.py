# positive_input.py

rejected_count = 0

while True:
    num = int(input("Введите положительное число: "))

    if num > 0:
        # Ввели верное число — выходим из цикла
        break
    else:
        # Неверный ввод — считаем ошибку
        rejected_count += 1

print(f"Квадрат числа: {num ** 2}")
print(f"Отклонённых попыток: {rejected_count}")