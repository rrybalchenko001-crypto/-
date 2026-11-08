"""Основная программа лабораторной работы №10."""

from pathlib import Path

from files_lab import read_matrix
from table import row_sums, column_sums
from variant import selected_sum


BASE_DIR = Path(__file__).resolve().parent
MATRIX_FILE = BASE_DIR / "matrix.txt"
REPORT_FILE = BASE_DIR / "report.txt"


def read_positive_integer(prompt: str = "Введите целое число больше нуля: ") -> int:
    """Запрашивает положительное целое число, пока пользователь не введёт корректное."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        if value <= 0:
            print("Ошибка: число должно быть больше нуля.")
            continue

        return value


def build_report(matrix: list[list[int]]) -> str:
    """Формирует полный текст отчёта по матрице."""
    rows = row_sums(matrix)
    columns = column_sums(matrix)
    variant_result = selected_sum(matrix)

    lines = [
        f"Суммы строк: {' '.join(map(str, rows))}",
        f"Суммы столбцов: {' '.join(map(str, columns))}",
        f"Результат варианта 1: {variant_result}",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    try:
        matrix = read_matrix(MATRIX_FILE)
        report = build_report(matrix)
        # Отчёт записывается только после успешного чтения и проверки матрицы.
        REPORT_FILE.write_text(report, encoding="utf-8")
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {MATRIX_FILE.name}")
    except (ValueError, OSError) as error:
        print(f"Ошибка обработки данных: {error}")
    else:
        print(f"Отчёт успешно сохранён в {REPORT_FILE.name}.")
        print(report, end="")


if __name__ == "__main__":
    main()
