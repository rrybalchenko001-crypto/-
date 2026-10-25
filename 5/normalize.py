text = input("Введите текст: ")

normalized = " ".join(text.split())

print("Исходная длина строки:", len(text))
print("Нормализованный текст:", normalized)
print("Количество слов:", len(normalized.split()))
