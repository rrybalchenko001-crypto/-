price = int(input("Введите цену тетради: "))
count = int(input("Введите количество: "))
paid = int(input("Введите переданную сумму: "))

cost = price * count
change = paid - cost

print(f"Стоимость {cost} , сдача {change}")
