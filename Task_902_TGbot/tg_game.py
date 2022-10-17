# Создайте программу для игры в "Крестики-нолики"

from random import randint
import config
import tg_keyboard

def clear_field():
    count = 1
    for i in range(0, 3):
        for k in range(0, 3):
            config.game_list[i][k] = str(count)
            count += 1
    tg_keyboard.BTN_GAME_1.text = '-'
    tg_keyboard.BTN_GAME_2.text = '-'
    tg_keyboard.BTN_GAME_3.text = '-'
    tg_keyboard.BTN_GAME_4.text = '-'
    tg_keyboard.BTN_GAME_5.text = '-'
    tg_keyboard.BTN_GAME_6.text = '-'
    tg_keyboard.BTN_GAME_7.text = '-'
    tg_keyboard.BTN_GAME_8.text = '-'
    tg_keyboard.BTN_GAME_9.text = '-'

def change_action(action):
    if action == 'X': config.action = 'O'
    elif action == 'O': config.action = 'X'
    return config.action

def change_field(number):
    for i in range(len(config.game_list)):
        for k in range(len(config.game_list[i])):
            if config.game_list[i][k] == number:
                config.game_list[i][k] = config.action
                break

def check_field(my_list: list) -> bool:
    config.count_action += 1
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