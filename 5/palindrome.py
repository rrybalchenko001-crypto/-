text = input("Введите текст: ")

# По условию игнорируем регистр и обычные пробелы.
cleaned = text.lower().replace(" ", "")

if cleaned == "":
    print("Нет текста")
elif cleaned == cleaned[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
