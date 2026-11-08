
"""Загрузка, проверка и сохранение JSON-файла."""

import json
import os
import tempfile
from pathlib import Path

from logic import validate_records


def load_records(path):
    """Загружает и проверяет записи из JSON. Пустой файл не считается корректным JSON."""
    path = Path(path)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    validate_records(records)
    return records


def save_records(path, records):
    """Сохраняет данные в UTF-8; временный файл защищает от частичной записи."""
    path = Path(path)
    validate_records(records)
    path.parent.mkdir(parents=True, exist_ok=True)

    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=path.parent,
            delete=False,
            suffix=".tmp",
        ) as temporary_file:
            json.dump(records, temporary_file, ensure_ascii=False, indent=4)
            temporary_file.write("\n")
            temporary_name = temporary_file.name

        os.replace(temporary_name, path)
    except Exception:
        if temporary_name and os.path.exists(temporary_name):
            os.remove(temporary_name)
        raise
