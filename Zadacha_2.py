# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])
# В скобках пример, как это работает!!!
mass1 = [2, 3, 4, 5, 6]
mass2 = [2, 3, 5, 6]


def parMult(mas):
    result = []
    count = len(mas)
    for i in range(int(count/2)):
        result.append(mas[i]*mas[int(-i-1)])
    if len(mas)/2 % 1 > 0:
        result.append(mas[int(len(mas)/2)]**2)
    print(result)


parMult(mass1)
parMult(mass2)