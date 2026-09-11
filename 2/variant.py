total = int(input("Введите общий объём: "))
capacity = int(input("Введите вместимость одной единицы: "))

full_units = total // capacity
remainder = total % capacity
total_units = (total + capacity - 1) // capacity

print(f"Полных {full_units} , остаток {remainder} , всего {total_units}")