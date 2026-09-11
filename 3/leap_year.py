year = int(input("Введите год от 1 до 9999: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("да")
else:
    print("нет")