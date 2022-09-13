# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Задать вопрос почему не сработало с ** 

import math

# Обычная последовательность чисел Фибоначчи
def fib(number: int) -> list:
    my_list = [0]
    for i in range(1, number + 1):
        if i == 1 or i == 2:
            my_list.append(1)
        else:
            my_list.append(my_list[i - 1] + my_list[i - 2])  
    
    return my_list

# Отношения к положительной последовательности чисел Фибоначчи: F(-n) = -1^(n+1) * F(n)
def neg_fib(my_list: list) -> list:
    new_list = []
    for i in range(1, len(my_list)):
        new_list.insert(0, pow(-1, (i + 1)) * my_list[i])
        
    return new_list + my_list

number = int(input('Введите число K: '))
print(neg_fib(fib(number)))
