# Функции для работы с матрицами


def row_sums(matrix):
    """Возвращает суммы элементов каждой строки."""
    result = []

    for row in matrix:
        result.append(sum(row))

    return result


def column_sums(matrix):
    """Возвращает суммы элементов каждого столбца."""
    result = []

    if len(matrix) == 0:
        return result

    for column in range(len(matrix[0])):
        total = 0
        for row in matrix:
            total += row[column]
        result.append(total)

    return result


def diagonal_pattern(size):
    """Создаёт узор: 0 на диагонали, 1 выше, 2 ниже."""
    result = []

    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(0)
            elif i < j:
                row.append(1)
            else:
                row.append(2)
        result.append(row)

    return result


def transform(matrix, variant=1):
    """Создаёт новую матрицу и выполняет выбранный вариант."""
    result = []

    for row in matrix:
        new_row = []

        for number in row:
            new_number = number

            if variant == 1:
                if number < 0:
                    new_number = 0

            elif variant == 2:
                if number > 0:
                    new_number = 1

            elif variant == 3:
                if number != 0 and number % 2 == 0:
                    new_number = number * 2

            elif variant == 4:
                if number % 2 != 0:
                    new_number = 0

            elif variant == 5:
                if number < 0:
                    new_number = abs(number)

            elif variant == 6:
                if number == 0:
                    new_number = 1

            elif variant == 7:
                if number > 0:
                    new_number = number + 5

            elif variant == 8:
                if number < 0:
                    new_number = number - 2

            elif variant == 9:
                if number != 0 and number % 3 == 0:
                    new_number = 3

            elif variant == 10:
                if abs(number) > 4:
                    new_number = 0

            elif variant == 11:
                if number != 0 and number % 2 == 0:
                    new_number = number // 2

            elif variant == 12:
                if number % 2 != 0:
                    new_number = number + 1

            elif variant == 13:
                if number > 0:
                    new_number = -number

            elif variant == 14:
                if -2 <= number <= 3:
                    new_number = number * number

            elif variant == 15:
                if number > 0:
                    new_number = 1
                elif number < 0:
                    new_number = -1

            new_row.append(new_number)

        result.append(new_row)

    return result
