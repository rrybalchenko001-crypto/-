"""Получение публичного профиля GitHub по логину через HTTP."""

import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


BASE_DIR = Path(__file__).resolve().parent
SAMPLE_FILE = BASE_DIR / "profile_sample.json"


def fetch_profile(login):
    """Возвращает данные GitHub-профиля или сообщает понятную ошибку."""
    if not login.strip():
        raise ValueError("Логин не должен быть пустым.")

    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "Python-Lab-11",
        },
    )

    try:
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        if error.code == 404:
            raise ValueError("Пользователь GitHub не найден.") from error
        if error.code == 403:
            raise ValueError("GitHub ограничил запрос (403).") from error
        raise ValueError(f"Ошибка HTTP: {error.code}.") from error
    except (URLError, socket.timeout, TimeoutError) as error:
        raise ConnectionError("Не удалось получить ответ от сети.") from error
    except json.JSONDecodeError as error:
        raise ValueError("Сервер вернул некорректный JSON.") from error

    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ сервера имеет неожиданный формат.")

    return data


def main():
    login = input("Логин GitHub: ").strip()

    try:
        profile = fetch_profile(login)
        output_file = BASE_DIR / "profile.json"
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(profile, file, ensure_ascii=False, indent=2)
        print("Профиль сохранён в profile.json")
        print("Имя:", profile.get("name"))
        print("Ссылка:", profile.get("html_url"))
    except (ValueError, ConnectionError, OSError) as error:
        print("Ошибка:", error)
        if SAMPLE_FILE.exists():
            print("Можно использовать profile_sample.json для работы без интернета.")


if __name__ == "__main__":
    main()
