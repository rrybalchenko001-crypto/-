# Дополнительное задание: факториал с помощью рекурсии


def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


assert factorial(0) == 1
assert factorial(5) == 120

print("Факториал числа 5:", factorial(5))
