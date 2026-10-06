# range_numbers.py

a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a <= b:
    # Идём вверх от a до b включительно
    for i in range(a, b + 1):
        print(i)
else:
    # Идём вниз от a до b включительно (шаг -1)
    for i in range(a, b - 1, -1):
        print(i)