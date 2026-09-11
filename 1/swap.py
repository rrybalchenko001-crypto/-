# Ввод данных
first_room = input("Введите первую аудиторию: ")
second_room = input("Введите вторую аудиторию: ")

# Вывод исходных значений
print(f"\nИсходные значения: первая = {first_room}, вторая = {second_room}")

# Обмен значений через третью переменную (temp)
temp = first_room
first_room = second_room
second_room = temp

# Вывод результата
print(f"После обмена: первая = {first_room}, вторая = {second_room}")