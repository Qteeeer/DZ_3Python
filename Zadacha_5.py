# 5'. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = int(input("Число размера последовательности: "))
a = []


def fibonacci_of(n):
    if n in {0, 1}:  
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  


def negativeFibonacci(num):
    result = []
    if num % 2 == 0:
        pn = -1
    else:
        pn = 1
    for i in range(-num, num+1):
        if i < 0:
            result.append(pn*fibonacci_of(-1*i))
            pn *= -1
        else:
            result.append(fibonacci_of(i))
    print(result)


negativeFibonacci(number)