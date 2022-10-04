# Создайте программу для игры в "Крестики-нолики"

from random import randint

def check_field(my_list: list) -> bool:
    result = False
    # горизонтальный поиск
    for i in range(len(my_list)):
        for k in range(len(my_list[i]) - 2):   
            if my_list[i][k] == my_list[i][k+1] and my_list[i][k] == my_list[i][k+2]:
                result = True
    # вертикальный поиск
    for i in range(len(my_list) - 2):
        for k in range(len(my_list[i])):
            if my_list[i][k] == my_list[i + 1][k] and my_list[i][k] == my_list[i + 2][k]:
                result = True
    # поиск по диагоналям
    for i in range(1, len(my_list) - 1):
        for k in range(1, len(my_list[i]) - 1):
            if my_list[i][k] == my_list[i - 1][k - 1] and my_list[i][k] == my_list[i + 1][k + 1]:
                result = True
            if my_list[i][k] == my_list[i - 1][k + 1] and my_list[i][k] == my_list[i + 1][k - 1]:
                result = True

    return result

print('--------------------')
print('Игра Крестики-нолики')
print('--------------------')

field = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

for i in field:
    print(i)

player = randint(1, 2)
print(f'Первым ходит игрок № {player}')
# mode = 2

count = 10
while count > 0:
    next_move = input(f'Игрок {player} введите номер клетки: ')
    if player == 1:
        for i in range(len(field)):
            for k in range(len(field[i])):               
                if next_move == field[i][k]:
                    field[i][k] = 'X'
                    player = 2
    if player == 2:
        for i in range(len(field)):
            for k in range(len(field[i])):               
                if next_move == field[i][k]:
                    field[i][k] = 'O'
                    player = 1

    for i in field:
        print(i)
    count -= 1
    if check_field(field):
        if player == 1: 
            player = 2
        elif player == 2: 
            player = 1 
        print(f'Игра окончена, победил {player} игрок')
        print('--------------------------------------')
        break  
    if count == 1:
        print(f'Игра окончена в ничью')
        break







