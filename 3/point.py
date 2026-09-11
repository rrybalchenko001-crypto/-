x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if 0 <= x <= 5 and 0 <= y <= 3:
    print("Внутри или на границе")
else:
    print("Снаружи")