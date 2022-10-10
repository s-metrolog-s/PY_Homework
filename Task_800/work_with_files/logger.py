from datetime import *

# Сохранение действий пользователя
def save_log(file_path, data):
    with open(f'{file_path}\log.csv', 'a', encoding = "utf_8") as file:
        result = f'{data};{datetime.now().strftime("%D:%H:%M:%S")}\n'
        print(result)
        file.write(result)