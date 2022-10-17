from aiogram import Bot, Dispatcher, executor, types
import config
import keys

import tg_keyboard
import weather
import math_commands as m_com
import tg_tube
from tg_log import save_log as log
import tg_game as game

# Инициализация бота и диспатчера
bot = Bot(token = keys.API_TOKEN)
dp = Dispatcher(bot)
print('Server starts')

# Основные команды
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    log(message.text)
    await message.answer("Hello\nI'm Bot!\nSend /help for all commands")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    log(message.text)
    await message.answer(
"""/start - Приветствие бота
/help - Список команд
/calc - Калькулятор
/weather - Погода
/getvideo - Скачать видео с Youtube
/game - Игра крестики-нолики""")

#-------------------------------------------------------------------------#
# Калькулятор

@dp.message_handler(commands=['calc'])
async def register_message_handler(message: types.Message):
    await message.answer(text='Выберите калькулятор для расчетов',
                         reply_markup=tg_keyboard.MAIN_CALC)

@dp.callback_query_handler(text = 'simple_calc')
async def process_callback_button1(callback_query: types.CallbackQuery):
    config.used_func = 1
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите выражение ввида: 2+4/2*3-5')

@dp.callback_query_handler(text = 'complex_calc')
async def process_callback_button2(callback_query: types.CallbackQuery):
    config.used_func = 2
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите выражение ввида: 1+3j*-1+7j')

#-------------------------------------------------------------------------#
# Погода

@dp.message_handler(commands=['weather'])
async def weather_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите название города:')
    config.used_func = 3
#-------------------------------------------------------------------------#
# Видео

@dp.message_handler(commands=['getvideo'])
async def register_message_handler(message: types.Message):
    await message.answer(text='Выберите формат видео для скачивания',
                         reply_markup=tg_keyboard.MAIN_VIDEO)

@dp.callback_query_handler(text = 'res_720p')
async def process_callback_button1(callback_query: types.CallbackQuery):
    config.used_func = 4
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вставьте ссылку Youtube:')

@dp.callback_query_handler(text = 'res_480p')
async def process_callback_button2(callback_query: types.CallbackQuery):
    config.used_func = 5
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вставьте ссылку Youtube:')

@dp.callback_query_handler(text = 'res_360p')
async def process_callback_button3(callback_query: types.CallbackQuery):
    config.used_func = 6
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вставьте ссылку Youtube:')

#-------------------------------------------------------------------------#
# Крестики-нолики

@dp.message_handler(commands=['game'])
async def register_message_handler(message: types.Message):
    log(message.text)
    await message.answer(text='Поставьте X в свободное поле',
                         reply_markup=tg_keyboard.MAIN_GAME)

@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
    current_action = config.action
    if callback_query.data == '1':
        tg_keyboard.BTN_GAME_1.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '2':
        tg_keyboard.BTN_GAME_2.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '3':
        tg_keyboard.BTN_GAME_3.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '4':
        tg_keyboard.BTN_GAME_4.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '5':
        tg_keyboard.BTN_GAME_5.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '6':
        tg_keyboard.BTN_GAME_6.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '7':
        tg_keyboard.BTN_GAME_7.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '8':
        tg_keyboard.BTN_GAME_8.text = config.action
        game.change_field(callback_query.data)
    elif callback_query.data == '9':
        tg_keyboard.BTN_GAME_9.text = config.action
        game.change_field(callback_query.data)

    print(config.game_list)

    if game.check_field(config.game_list):
        await bot.send_message(callback_query.from_user.id, f'Игра окончена',
                         reply_markup=tg_keyboard.MAIN_GAME)
        game.clear_field()
        await bot.send_message(callback_query.from_user.id, f'Выиграл игрок {config.action}')
    else:
        if config.count_action == 7:
            await bot.send_message(callback_query.from_user.id, f'Игра окончена в ничью',
                            reply_markup=tg_keyboard.MAIN_GAME)
            game.clear_field()
        else:
        # await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, f'Поставьте {game.change_action(current_action)} в свободное поле',
                            reply_markup=tg_keyboard.MAIN_GAME)
#-------------------------------------------------------------------------#
# Обработчик входящих сообщений

@dp.message_handler()
async def echo_message(message: types.Message):
    if config.used_func == 1:
        log(f'/simple_calc {message.text}')
        await bot.send_message(message.from_user.id, m_com.simple_calc(message.text))
    if config.used_func == 2:
        log(f'/complex_calc {message.text}')
        await bot.send_message(message.from_user.id, m_com.complex_calc(message.text))
    if config.used_func == 3:
        log(f'/weather {message.text}')
        await bot.send_message(message.from_user.id, weather.weather_checker(message.text))
    if config.used_func == 4:
        log(f'/getvideo {message.text}')
        await bot.send_document(message.from_user.id, open(tg_tube.video_download(message.text, '720p'), 'rb'),
                            caption='Видео успешно загрузилось!')
    if config.used_func == 5:
        log(f'/getvideo {message.text}')
        await bot.send_document(message.from_user.id, open(tg_tube.video_download(message.text, '480p'), 'rb'),
                            caption='Видео успешно загрузилось!')
    if config.used_func == 6:
        log(f'/getvideo {message.text}')
        await bot.send_document(message.from_user.id, open(tg_tube.video_download(message.text, '360p'), 'rb'),
                            caption='Видео успешно загрузилось!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)