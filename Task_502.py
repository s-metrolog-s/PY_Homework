# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
from time import sleep

# Проверка введенной пользователем информации
def check_input(x: int, y: int) -> int: 
    while x < 1 or x > 28:
        print(f'Введенное число {x} не входит в диапазон условия')
        x = int(input('Введите число от 1 до 28: '))
    while x > y:
        print(f'Осталось всего {y} конфет')
        x = int(input(f'Введите число от 1 до {y}: '))
    return x, y

# Условие по количеству конфет и жеребьевка
sweet_count = 221
print('Приветствуем вас в игре - "Выиграй все конфеты"\nПобеждает тот, кто ходит последний')
print(f'В игре участвует {sweet_count} конфет')

player = randint(1, 2)
print('Проведем жеребьевку...')
print(f'Первым ходит игрок № {player}')

# Выбор режима игры
print('Выберите режим игры:\n1 - человек с человеком\n2 - человек против компьютера\n3 - компьютер против компьютера')
mode_of_play = int(input())
print('----------------------------------')

# Вариант игры человек против человека
if mode_of_play == 1:
    while sweet_count > 0:
        step = int(input(f'Ходит {player} игрок, число от 1 до 28: '))
        step, sweet_count = check_input(step, sweet_count)
        sweet_count -= step
        print(f'Конфет осталось {sweet_count}')
        if sweet_count == 0:
            print('----------------------------------')
            print(f'Игрок {player} одерживает победу!')
            print('----------------------------------')
            continue
        if player == 1: player = 2
        elif player == 2: player = 1
        print('------------------------------')

# Вариант игры человек против компьютера
elif mode_of_play == 2:
    while sweet_count > 0:
        if player == 1:
            step = int(input(f'Ходит {player} игрок, число от 1 до 28: '))
            step, sweet_count = check_input(step, sweet_count)
            sweet_count -= step      
        
        if player == 2:
            print(f'Ходит компьютер, число от 1 до 28: ', end = '')
            sleep(1)
            #step = randint(1, 28) Вариант без математики
            step = sweet_count % 29
            if step == 0: step = 1
            sweet_count -= step
            print(f'{step}')
            sleep(1)
        
        print(f'Конфет осталось {sweet_count}')

        if sweet_count == 0:
            print('----------------------------------')
            print(f'Игрок {player} одерживает победу!')
            print('----------------------------------')
            continue

        if player == 1: player = 2
        elif player == 2: player = 1
        print('------------------------------')

# Вариант игры компьютер против компьютера
elif mode_of_play == 3:
    while sweet_count > 0:
        if player == 1:
            print(f'Ходит игрок {player}, число от 1 до 28: ', end = '')
            sleep(1)
            step = randint(1, 28) #Вариант без математики
            #step = sweet_count % 29
            if step == 0: step = 1
            sweet_count -= step
            print(f'{step}')
            sleep(1)     
        
        if player == 2:
            print(f'Ходит игрок {player}, число от 1 до 28: ', end = '')
            sleep(1)
            #step = randint(1, 28) Вариант без математики
            step = sweet_count % 29
            if step == 0: step = 1
            sweet_count -= step
            print(f'{step}')
            sleep(1)
        
        print(f'Конфет осталось {sweet_count}')

        if sweet_count == 0:
            print('----------------------------------')
            print(f'Игрок {player} одерживает победу!')
            print('----------------------------------')
            continue

        if player == 1: player = 2
        elif player == 2: player = 1
        print('------------------------------')
else:   
    print('Не выбран ни один из возможных режимов игры, работа программы завершена')
