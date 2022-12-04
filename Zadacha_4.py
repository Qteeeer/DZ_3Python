# 4'. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

inputNumber = int(input("Введите число: "))


def binar(number):

    result = ""
    while number != 0:
        result = str(number % 2) + result
        number //= 2
    print(result)


binar(inputNumber)