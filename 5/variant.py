# Индивидуальное задание: обработка слов по выбранному варианту.
# Сначала удаляем знаки пунктуации только с краёв слова,
# затем переводим слово в нижний регистр.
PUNCTUATION = ".,!?;:"
VOWELS = "аеёиоуыэюя"

def matches(word, variant):
    if variant == 1:
        return word.startswith("а")
    if variant == 2:
        return word.endswith("я")
    if variant == 3:
        return len(word) >= 5
    if variant == 4:
        return word.startswith("к")
    if variant == 5:
        return word.endswith("а")
    if variant == 6:
        return len(word) == 4
    if variant == 7:
        return "р" in word
    if variant == 8:
        return word.count("а") == 1
    if variant == 9:
        return "а" not in word
    if variant == 10:
        return word[0] == word[-1]
    if variant == 11:
        return 3 <= len(word) <= 5
    if variant == 12:
        return "ра" in word
    if variant == 13:
        return word.endswith("й")
    if variant == 14:
        return len(word) % 2 == 0
    if variant == 15:
        return word[0] in VOWELS
    return False

try:
    variant = int(input("Введите номер варианта (1–15): "))
except ValueError:
    print("Ошибка: номер варианта должен быть целым числом.")
    raise SystemExit

if not 1 <= variant <= 15:
    print("Ошибка: выберите вариант от 1 до 15.")
    raise SystemExit

text = input("Введите строку: ")
words = []

for raw_word in text.split():
    word = raw_word.strip(PUNCTUATION).lower()

    # Пропускаем слова, которые после очистки стали пустыми.
    if word and matches(word, variant):
        words.append(word)

if words:
    print("Подходящие слова:")
    for word in words:
        print(word)
else:
    print("Нет совпадений")

print("Количество:", len(words))
