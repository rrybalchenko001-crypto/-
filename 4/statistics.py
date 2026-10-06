# statistics.py

n = int(input("Введите количество чисел n: "))

# Считываем самое первое число
first_num = int(input())

# Инициализируем переменные
total = first_num
maximum = first_num

if first_num > 0:
    positives = 1
else:
    positives = 0

# Считываем оставшиеся n - 1 чисел
for _ in range(n - 1):
    num = int(input())
    total += num

    if num > 0:
        positives += 1

    if num > maximum:
        maximum = num

print(f"Сумма: {total}")
print(f"Количество положительных: {positives}")
print(f"Максимум: {maximum}")