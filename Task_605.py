# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odds_index(my_list: list) -> int:
    sum = 0
    for i in range(1, len(my_list), 2):
        sum += my_list[i]
    return sum

my_list = [2, 3, 5, 9, 3, 1, 7]
new_list = my_list.copy()

print(f'Дан список: {my_list}')
print('Ищем сумму нечетных элементов...')
print(f'Сумма равна: {sum_odds_index(my_list)}')

# Короткое решение
res = [v for i, v in enumerate(new_list) if i % 2 == 1]
print(f'Сумма равна: {sum(res)}')