# Реализуйте алгоритм перемешивания списка
from random import randint

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mix_list = []
print(f'Дан список: {list_1}')
print('Перемешаем его как следует...')

# перемешивание списка через Random
while list_1 != []:
    item = randint(0, len(list_1)-1)
    mix_list.append(list_1.pop(item))

print(f'Готовый список: {mix_list}')

