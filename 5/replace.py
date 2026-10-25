text = input("Введите текст: ")

count = text.count(":")
new_text = text.replace(":", "-")

print("Количество замен:", count)
print("Новая строка:", new_text)
