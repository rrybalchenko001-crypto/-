"""Интерактивный запуск лабораторной работы № 8, индивидуальный вариант 8."""

from collections_lab import (
    records,
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    update_record_amount,
)


def main() -> None:
    print("Частоты слов:", word_counts("Python, python! SQL"))
    print("Общие темы:", common_topics(["Python", "SQL", "Python"], ["SQL", "Git"]))
    print("Все темы:", all_topics(["Python", "SQL"], ["SQL", "Git"]))

    print("\nЗаписи индивидуального варианта 8 (настольные игры):")
    for record in records:
        print(record)

    print("\nСуммы amount по категориям:", totals_by_category(records))
    category = input("\nВведите категорию для поиска: ").strip()
    titles = titles_in_category(records, category)
    if titles:
        print("Названия по алфавиту:", titles)
    else:
        print("Категория не найдена: []")

    # Демонстрация поверхностного копирования словаря.
    updated = update_record_amount(records[0], 6)
    print("\nИсходная запись:", records[0])
    print("Копия с изменённым amount:", updated)


if __name__ == "__main__":
    main()
