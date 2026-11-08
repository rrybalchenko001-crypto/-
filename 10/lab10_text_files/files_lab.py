"""Чтение и проверка матрицы из текстового файла."""

from pathlib import Path


def read_matrix(path: str | Path) -> list[list[int]]:
    """Считывает матрицу из файла и проверяет её формат.

    Формат:
        первая строка: количество строк и столбцов (два положительных числа);
        далее ровно указанное количество строк матрицы;
        в каждой строке ровно указанное количество целых чисел.

    Пустые строки, лишние строки и неверное количество элементов запрещены.
    """
    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    if not lines:
        raise ValueError("Файл пуст.")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Заголовок должен содержать два числа: количество строк и столбцов.")

    try:
        row_count, column_count = map(int, header)
    except ValueError as error:
        raise ValueError("В заголовке должны быть целые числа.") from error

    if row_count <= 0 or column_count <= 0:
        raise ValueError("Количество строк и столбцов должно быть больше нуля.")

    data_lines = lines[1:]
    if len(data_lines) != row_count:
        raise ValueError(
            f"Ожидалось строк матрицы: {row_count}, получено: {len(data_lines)}."
        )

    matrix: list[list[int]] = []
    for line_number, line in enumerate(data_lines, start=2):
        parts = line.split()
        if not parts:
            raise ValueError(f"Пустая строка матрицы: строка {line_number}.")

        if len(parts) != column_count:
            raise ValueError(
                f"Строка {line_number}: ожидалось чисел {column_count}, "
                f"получено {len(parts)}."
            )

        try:
            matrix_row = [int(part) for part in parts]
        except ValueError as error:
            raise ValueError(
                f"Строка {line_number}: все элементы должны быть целыми числами."
            ) from error

        matrix.append(matrix_row)

    return matrix
