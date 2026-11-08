from table import row_sums, column_sums, diagonal_pattern, transform


# Проверка сумм строк и столбцов
matrix = [[1, 2, 3], [4, 5, 6]]

assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]


# Проверка диагонального узора
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0]
]


# Проверка всех вариантов на контрольной матрице
control = [[-2, 0, 3], [4, -5, 6]]

assert transform(control, 1) == [[0, 0, 3], [4, 0, 6]]
assert transform(control, 2) == [[-2, 0, 1], [1, -5, 1]]
assert transform(control, 3) == [[-4, 0, 3], [8, -5, 12]]
assert transform(control, 4) == [[-2, 0, 0], [4, 0, 6]]
assert transform(control, 5) == [[2, 0, 3], [4, 5, 6]]
assert transform(control, 6) == [[-2, 1, 3], [4, -5, 6]]
assert transform(control, 7) == [[-2, 0, 8], [9, -5, 11]]
assert transform(control, 8) == [[-4, 0, 3], [4, -7, 6]]
assert transform(control, 9) == [[-2, 0, 3], [4, -5, 3]]
assert transform(control, 10) == [[-2, 0, 3], [4, 0, 0]]
assert transform(control, 11) == [[-1, 0, 3], [2, -5, 3]]
assert transform(control, 12) == [[-2, 0, 4], [4, -4, 6]]
assert transform(control, 13) == [[-2, 0, -3], [-4, -5, -6]]
assert transform(control, 14) == [[4, 0, 9], [4, -5, 6]]
assert transform(control, 15) == [[-1, 0, 1], [1, -1, 1]]


# Проверка, что исходная матрица не изменилась
assert matrix == [[1, 2, 3], [4, 5, 6]]

print("Все тесты пройдены успешно!")
