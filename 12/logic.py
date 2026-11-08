
"""Логика работы с записями туристических маршрутов."""


def validate_records(records):
    """Проверяет структуру и значения всех записей; возвращает True или вызывает ValueError."""
    if not isinstance(records, list):
        raise ValueError("Корневой элемент JSON должен быть списком.")

    used_ids = set()
    required_keys = {"id", "title", "category", "amount", "completed"}

    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Запись №{index} должна быть объектом.")
        if set(record.keys()) != required_keys:
            raise ValueError(
                f"Запись №{index} должна содержать только поля: "
                "id, title, category, amount, completed."
            )

        record_id = record["id"]
        if isinstance(record_id, bool) or not isinstance(record_id, int) or record_id <= 0:
            raise ValueError(f"В записи №{index} ID должен быть положительным целым числом.")
        if record_id in used_ids:
            raise ValueError(f"Обнаружен повторяющийся ID: {record_id}.")
        used_ids.add(record_id)

        for field in ("title", "category"):
            value = record[field]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Поле «{field}» в записи №{index} не должно быть пустым.")

        amount = record["amount"]
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise ValueError(f"Длина маршрута в записи №{index} должна быть целым числом километров.")
        if amount < 0:
            raise ValueError(f"Длина маршрута в записи №{index} не может быть отрицательной.")

        if not isinstance(record["completed"], bool):
            raise ValueError(f"Статус completed в записи №{index} должен быть true или false.")

    return True


def next_id(records):
    """Возвращает следующий ID, не переиспользуя ID удалённых записей."""
    if not records:
        return 1
    return max(record["id"] for record in records) + 1


def add_record(records, title, category, amount):
    """Добавляет маршрут и возвращает созданную запись."""
    title = title.strip() if isinstance(title, str) else ""
    category = category.strip() if isinstance(category, str) else ""

    if not title:
        raise ValueError("Название маршрута не может быть пустым.")
    if not category:
        raise ValueError("Категория маршрута не может быть пустой.")
    if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
        raise ValueError("Длина маршрута должна быть неотрицательным целым числом километров.")

    validate_records(records)
    record = {
        "id": next_id(records),
        "title": title,
        "category": category,
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    """Ищет записи без учёта регистра по названию и категории."""
    query = query.strip().casefold()
    if not query:
        return []
    return [
        record for record in records
        if query in record["title"].casefold()
        or query in record["category"].casefold()
    ]


def set_completed(records, record_id, completed):
    """Изменяет статус маршрута по ID."""
    if not isinstance(completed, bool):
        raise ValueError("Статус должен быть логическим значением.")
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return record
    raise ValueError(f"Маршрут с ID {record_id} не найден.")


def delete_record(records, record_id):
    """Удаляет маршрут по ID и возвращает удалённую запись."""
    for index, record in enumerate(records):
        if record["id"] == record_id:
            return records.pop(index)
    raise ValueError(f"Маршрут с ID {record_id} не найден.")


def statistics(records):
    """Считает статистику по текущему списку записей."""
    completed_records = [record for record in records if record["completed"]]
    total_amount = sum(record["amount"] for record in records)
    completed_amount = sum(record["amount"] for record in completed_records)
    return {
        "total": len(records),
        "completed": len(completed_records),
        "not_completed": len(records) - len(completed_records),
        "total_amount": total_amount,
        "completed_amount": completed_amount,
    }
