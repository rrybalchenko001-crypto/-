
"""Главный модуль консольной программы «План туристических маршрутов»."""

from pathlib import Path

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
)
from storage import load_records, save_records, validate_records

DATA_FILE = Path(__file__).with_name("data.json")


def show_records(records):
    """Выводит все маршруты в виде таблицы."""
    if not records:
        print("\nСписок маршрутов пуст.")
        return

    print("\n" + "-" * 82)
    print(f"{'ID':<5}{'Название':<28}{'Категория':<18}{'Км':>10}  {'Статус':<15}")
    print("-" * 82)
    for record in records:
        status = "Пройден" if record["completed"] else "Не пройден"
        print(
            f"{record['id']:<5}"
            f"{record['title'][:26]:<28}"
            f"{record['category'][:16]:<18}"
            f"{record['amount']:>10}  "
            f"{status:<15}"
        )
    print("-" * 82)


def read_amount():
    """Запрашивает корректную длину маршрута."""
    while True:
        raw_value = input("Длина маршрута (км): ").strip().replace(",", ".")
        try:
            amount = int(raw_value)
            if amount < 0:
                print("Ошибка: длина не может быть отрицательной.")
                continue
            return amount
        except ValueError:
            print("Ошибка: введите целое число километров, например 12.")


def read_id():
    """Запрашивает положительный целочисленный ID."""
    while True:
        raw_value = input("Введите ID: ").strip()
        try:
            record_id = int(raw_value)
            if record_id <= 0:
                print("ID должен быть положительным числом.")
                continue
            return record_id
        except ValueError:
            print("Ошибка: ID должен быть целым числом.")


def save_current(records):
    """Сохраняет список и сообщает об ошибке, не завершая программу."""
    try:
        save_records(DATA_FILE, records)
        print("Данные успешно сохранены.")
        return True
    except (OSError, ValueError, TypeError) as error:
        print(f"Не удалось сохранить данные: {error}")
        print("Данные остаются в памяти программы.")
        return False


def main():
    try:
        records = load_records(DATA_FILE)
    except (OSError, ValueError, TypeError) as error:
        print(f"Не удалось загрузить data.json: {error}")
        print("Программа запущена с пустым списком. Исходный файл не перезаписан.")
        records = []

    while True:
        print(
            "\n=== ПЛАН ТУРИСТИЧЕСКИХ МАРШРУТОВ ===\n"
            "1. Показать все маршруты\n"
            "2. Добавить маршрут\n"
            "3. Найти маршрут по названию или категории\n"
            "4. Изменить статус маршрута\n"
            "5. Удалить маршрут\n"
            "6. Показать статистику\n"
            "7. Сохранить данные\n"
            "0. Выход"
        )
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_records(records)

        elif choice == "2":
            title = input("Название маршрута: ").strip()
            category = input("Категория (например, пеший, горный): ").strip()
            amount = read_amount()
            try:
                record = add_record(records, title, category, amount)
                print(f"Маршрут добавлен. Присвоен ID: {record['id']}.")
            except ValueError as error:
                print(f"Ошибка: {error}")

        elif choice == "3":
            query = input("Введите часть названия или категории: ").strip()
            if not query:
                print("Поисковый запрос не может быть пустым.")
            else:
                found = find_records(records, query)
                if found:
                    show_records(found)
                else:
                    print("Ничего не найдено.")

        elif choice == "4":
            record_id = read_id()
            value = input("Новый статус (1 — пройден, 0 — не пройден): ").strip()
            if value not in ("0", "1"):
                print("Ошибка: введите только 1 или 0.")
            else:
                try:
                    set_completed(records, record_id, value == "1")
                    print("Статус маршрута изменён.")
                except ValueError as error:
                    print(f"Ошибка: {error}")

        elif choice == "5":
            record_id = read_id()
            answer = input(f"Удалить маршрут с ID {record_id}? (да/нет): ").strip().lower()
            if answer in ("да", "д", "yes", "y"):
                try:
                    delete_record(records, record_id)
                    print("Маршрут удалён.")
                except ValueError as error:
                    print(f"Ошибка: {error}")
            else:
                print("Удаление отменено.")

        elif choice == "6":
            stats = statistics(records)
            print("\n=== СТАТИСТИКА ===")
            print(f"Всего маршрутов: {stats['total']}")
            print(f"Пройдено: {stats['completed']}")
            print(f"Не пройдено: {stats['not_completed']}")
            print(f"Общая длина всех маршрутов: {stats['total_amount']} км")
            print(f"Длина пройденных маршрутов: {stats['completed_amount']} км")

        elif choice == "7":
            save_current(records)

        elif choice == "0":
            answer = input("Сохранить текущие данные перед выходом? (да/нет): ").strip().lower()
            if answer in ("да", "д", "yes", "y"):
                if not save_current(records):
                    print("Вы можете вернуться в меню и повторить сохранение.")
                    continue
            print("Работа программы завершена.")
            break

        else:
            print("Неизвестная команда. Выберите пункт от 0 до 7.")


if __name__ == "__main__":
    main()
