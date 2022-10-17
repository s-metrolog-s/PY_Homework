from datetime import *
from pathlib import Path

# Сохранение действий пользователя
def save_log(data):
    file_path = Path.cwd()
    command = data.split()
    with open(f'{file_path}\log.csv', 'a', encoding = "utf_8") as file:
        if len(command) == 1: param = ''
        else: param = command[1]
        result = f'Команда-{command[0]};Запрос-{param};{datetime.now().strftime("%D:%H:%M:%S")}\n'
        print(result)
        file.write(result)