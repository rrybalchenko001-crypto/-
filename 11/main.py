"""Основная программа: чтение JSON, анализ и сохранение результата."""

import json
from pathlib import Path

from analysis import validate_todos, completed_counts, leaders, select_tasks


BASE_DIR = Path(__file__).resolve().parent
TODOS_FILE = BASE_DIR / "todos.json"
LEADERS_FILE = BASE_DIR / "leaders.json"


def read_positive_integer(prompt):
    """Запрашивает положительное целое число с повтором при ошибке."""
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Введите целое число.")
            continue

        if number <= 0:
            print("Число должно быть больше нуля.")
            continue

        return number


def main():
    try:
        with open(TODOS_FILE, "r", encoding="utf-8") as file:
            todos = json.load(file)

        validate_todos(todos)

        print("Количество выполненных задач по пользователям:")
        counts = completed_counts(todos)
        for user_id, count in sorted(counts.items()):
            print(f"Пользователь {user_id}: {count}")

        best_users = leaders(todos)
        with open(LEADERS_FILE, "w", encoding="utf-8") as file:
            json.dump(best_users, file, ensure_ascii=False, indent=2)

        print("Лидеры сохранены в leaders.json:", best_users)

        user_id = read_positive_integer("Введите user_id: ")
        user_tasks = select_tasks(todos, user_id)
        print("Задачи выбранного пользователя:")
        print(json.dumps(user_tasks, ensure_ascii=False, indent=2))

    except FileNotFoundError:
        print("Ошибка: файл todos.json не найден.")
    except json.JSONDecodeError as error:
        print("Ошибка JSON:", error)
    except ValueError as error:
        print("Ошибка в данных:", error)
    except OSError as error:
        print("Ошибка работы с файлом:", error)


if __name__ == "__main__":
    main()
