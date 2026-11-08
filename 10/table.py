"""Функции обработки двумерных таблиц (матриц)."""


def row_sums(matrix: list[list[int]]) -> list[int]:
    """Возвращает суммы элементов каждой строки."""
    return [sum(row) for row in matrix]


def column_sums(matrix: list[list[int]]) -> list[int]:
    """Возвращает суммы элементов каждого столбца."""
    if not matrix:
        return []
    return [sum(row[column] for row in matrix) for column in range(len(matrix[0]))]
