# 3'. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
mass = [1.1, 1.2, 3.1, 5, 10.01]


def maxDif(mas):
    mutable = [round(i % 1, 2) for i in mas if i % 1 != 0]
    print(max(mutable)-min(mutable))


maxDif(mass)