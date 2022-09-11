# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_pair_index(my_list: list) -> list:
    mult_list = []
    count = 0
    if (len(my_list) % 2) == 0:
        for i in range(len(my_list)//2 - count):
            mult_list.append(my_list[i] * my_list[-1-count])
            count += 1
    else:
        for i in range(len(my_list)//2+1 - count):
            mult_list.append(my_list[i] * my_list[-1-count])
            count += 1

    return mult_list

def mult_pair_index_ver_2(my_list: list) -> list:
    mult_list = []
    index = 0
    count = len(my_list) - 1
    while index <= count:
        mult_list.append(my_list[index] * my_list[count])
        index += 1
        count -= 1
    return mult_list

my_list_1 = [2, 3, 4, 5, 6]
my_list_2 = [2, 3, 5, 6]

print(f'Дан список 1: {my_list_1}')
print(f'Дан список 2: {my_list_2}')
print('Посчитаем произведение пар чисел по условию...')

print(f'Произведение пар 1 списка {mult_pair_index(my_list_1)}')
print(f'Произведение пар 2 списка {mult_pair_index(my_list_2)}')

print(f'Произведение пар 1 списка вторым способом {mult_pair_index_ver_2(my_list_1)}')
print(f'Произведение пар 2 списка вторым способом {mult_pair_index_ver_2(my_list_2)}')