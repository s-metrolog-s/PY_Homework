# Задайте последовательность чисел. 
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 7, 4, 5, 7, 5] -> [2, 3, 4]

def check_unique_element(my_list: list) -> list:
    result_list = []
    for i in my_list:
        if (i not in result_list) and (my_list.count(i) < 2):
            result_list.append(i)
    return result_list

my_list = [1, 1, 2, 3, 'text', 3, 7, 4, 'main', 5, 7, 5, 'text']

print(f'Дан следующий список: {my_list}')
print('Выведем список неповторяющихся элементов...')
print(f'Новый список: {check_unique_element(my_list)}')

# Более короткое решение
print('Решение с помощью lambda + filter: ', end = '')
res = list(filter(lambda x: my_list.count(x) == 1, my_list))
print(res)