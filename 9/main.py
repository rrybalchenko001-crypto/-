from table import row_sums, column_sums, diagonal_pattern, transform


# Ввод матрицы
rows = int(input("Количество строк: "))
columns = int(input("Количество столбцов: "))

matrix = []

for i in range(rows):
    while True:
        numbers = list(map(int, input(
            "Введите элементы строки через пробел: "
        ).split()))

        if len(numbers) == columns:
            matrix.append(numbers)
            break
        else:
            print("В строке должно быть", columns, "чисел. Повторите ввод.")

print("\nИсходная матрица:")
for row in matrix:
    print(row)


# Суммы строк и столбцов
print("\nСуммы строк:", row_sums(matrix))
print("Суммы столбцов:", column_sums(matrix))


# Диагональный узор
size = int(input("\nВведите размер диагонального узора: "))

while size <= 0:
    size = int(input("Размер должен быть положительным. Повторите ввод: "))

pattern = diagonal_pattern(size)

print("\nДиагональный узор:")
for row in pattern:
    print(row)


# Индивидуальное преобразование
variant = int(input("\nВведите номер своего варианта (1–15): "))

while variant < 1 or variant > 15:
    variant = int(input("Введите номер от 1 до 15: "))

new_matrix = transform(matrix, variant)

print("\nНовая матрица:")
for row in new_matrix:
    print(row)

print("\nИсходная матрица не изменилась:")
for row in matrix:
    print(row)
