from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура Калькулятора
BTN_SIMPLE_CALC = InlineKeyboardButton('Простой', callback_data='simple_calc')
BTN_COMPLEX_CALC = InlineKeyboardButton('Комплексный', callback_data='complex_calc')

MAIN_CALC = InlineKeyboardMarkup().add(BTN_SIMPLE_CALC, BTN_COMPLEX_CALC)

# Клавиатура для скачивания видео
BTN_720P = InlineKeyboardButton('720p', callback_data='res_720p')
BTN_480P = InlineKeyboardButton('480p', callback_data='res_480p')
BTN_360P = InlineKeyboardButton('360p', callback_data='res_360p')

MAIN_VIDEO = InlineKeyboardMarkup().add(BTN_720P, BTN_480P, BTN_360P)

# Крестики-нолики
BTN_GAME_1 = InlineKeyboardButton('-', callback_data='1')
BTN_GAME_2 = InlineKeyboardButton('-', callback_data='2')
BTN_GAME_3 = InlineKeyboardButton('-', callback_data='3')
BTN_GAME_4 = InlineKeyboardButton('-', callback_data='4')
BTN_GAME_5 = InlineKeyboardButton('-', callback_data='5')
BTN_GAME_6 = InlineKeyboardButton('-', callback_data='6')
BTN_GAME_7 = InlineKeyboardButton('-', callback_data='7')
BTN_GAME_8 = InlineKeyboardButton('-', callback_data='8')
BTN_GAME_9 = InlineKeyboardButton('-', callback_data='9')

MAIN_GAME = InlineKeyboardMarkup().add(BTN_GAME_1, BTN_GAME_2, BTN_GAME_3).add(BTN_GAME_4, 
                                BTN_GAME_5, BTN_GAME_6).add(BTN_GAME_7, BTN_GAME_8, BTN_GAME_9)