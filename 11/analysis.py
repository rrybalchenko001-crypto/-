"""Проверка и обработка списка задач из JSON."""

def validate_todos(data):
    """Проверяет структуру списка задач. При ошибке вызывает ValueError."""
    if not isinstance(data, list):
        raise ValueError("В корне JSON должен находиться список.")

    for number, todo in enumerate(data, start=1):
        if not isinstance(todo, dict):
            raise ValueError(f"Запись {number} должна быть объектом.")

        for field in ("id", "userId"):
            value = todo.get(field)
            if type(value) is not int or value <= 0:
                raise ValueError(
                    f"Запись {number}: поле {field} должно быть положительным целым числом."
                )

        if not isinstance(todo.get("title"), str) or not todo["title"].strip():
            raise ValueError(f"Запись {number}: title должен быть непустой строкой.")

        if type(todo.get("completed")) is not bool:
            raise ValueError(f"Запись {number}: completed должен быть true или false.")

    return data


def completed_counts(todos):
    """Возвращает словарь: userId -> количество выполненных задач."""
    counts = {}
    for todo in todos:
        user_id = todo["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        if todo["completed"]:
            counts[user_id] += 1
    return counts


def leaders(todos):
    """Возвращает всех пользователей с максимальным числом выполненных задач."""
    counts = completed_counts(todos)
    if not counts:
        return []

    maximum = max(counts.values())
    return sorted(user_id for user_id, count in counts.items() if count == maximum)


def select_tasks(todos, user_id, parameter=None):
    """Индивидуальный вариант 1: все задачи выбранного пользователя.

    parameter оставлен для общего интерфейса вариантов; для варианта 1 не нужен.
    """
    return [todo for todo in todos if todo["userId"] == user_id]
