# Предмет 1
sub1_name = input("Предмет 1: ")
sub1_count = int(input("Занятий в неделю: "))
sub1_dur = int(input("Длительность занятия (мин): "))

# Предмет 2
sub2_name = input("Предмет 2: ")
sub2_count = int(input("Занятий в неделю: "))
sub2_dur = int(input("Длительность занятия (мин): "))

# Расчеты
sub1_min = sub1_count * sub1_dur
sub2_min = sub2_count * sub2_dur
total_min = sub1_min + sub2_min
total_hours = total_min / 60

# Ввод доступного времени (указывай не меньше total_hours)
avail_hours = float(input(f"Доступно часов в неделю (не меньше {total_hours:.2f}): "))

# Вывод
print("\n--- УЧЕБНАЯ НАГРУЗКА ---")
print(f"Время на {sub1_name}: {sub1_min} мин.")
print(f"Время на {sub2_name}: {sub2_min} мин.")
print(f"Общая нагрузка: {total_min} мин. ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {avail_hours - total_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {total_hours * 4:.2f} ч.")
