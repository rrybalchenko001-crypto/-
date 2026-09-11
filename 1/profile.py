# Ввод данных
last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (1-120): "))
subject = input("Любимый предмет: ")
hours = float(input("Часов подготовки в неделю: "))

# Карточка
print("\n--- КАРТОЧКА СТУДЕНТА ---")
print(f"Имя и фамилия: {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст через 4 года: {age + 4}")
print(f"Любимый предмет: {subject}")
print(f"Подготовка за 4 недели: {hours * 4:.2f} ч.")
print(f"Среднее время в день: {hours / 7:.2f} ч.")