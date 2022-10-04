# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def make_list() -> list:
    my_list = []
    for i in range(random.randint(5, 10)):
        my_list.append(round((random.randint(1, 10) + random.random()), 3))
    return my_list

def min_max_fraction(my_list: list) -> float:
    for i in range(len(my_list)):
        my_list[i] = my_list[i] % int(my_list[i])
    min_value = 0
    max_value = 0
    for i in range(len(my_list)):
        if my_list[i] > my_list[max_value]:
            max_value = i
        if my_list[i] < my_list[min_value]:
            min_value = i
    result = my_list[max_value] - my_list[min_value]
    return round(result, 3)

my_list = [1.1, 1.2, 3.1, 5.07, 10.01]
second_list = make_list()
new_list = second_list.copy()

print(f'Дан список: {my_list}')
print(f'Разница между max и min значением дробной части равно: {min_max_fraction(my_list)}')

print(f'Дан список: {second_list}')
print(f'Разница между max и min значением дробной части равно: {min_max_fraction(second_list)}')

# Более короткое решение
result = list(map(lambda x: round(x % int(x), 3), new_list))
print(f'(lambda + map) Разница Max - Min = {max(result) - min(result)}')