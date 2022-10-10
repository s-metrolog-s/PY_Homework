# Запись и чтение из базы данных

from encodings import utf_8
from re import L
from work_with_files import id_functions as id_func
from work_with_files import logger as log

# Добавление новой записи в базу данных
def add_row(file_path, file_format, data):
    if file_format == 1: file_format = 'csv'
    elif file_format == 2: file_format = 'txt'
    
    with open(f'{file_path}\data\data.{file_format}', 'a', encoding = "utf_8") as file:
            result = ';'.join(data) + '\n'
            file.write(result)
    log.save_log(file_path, f'Save_row_to_dbase: {result[:-2]}')
    id_func.check_id(file_path, file_format)
    copy_dbase(file_path, file_format)
    
# Поиск записи в базе данных
def find_string(file_path: str, file_format: int, data_find: str) -> str:
    if file_format == 1: file_format = 'csv'
    elif file_format == 2: file_format = 'txt'
    
    with open(f'{file_path}\data\data.{file_format}', 'r', encoding = "utf_8") as file:
        for line in file:
            if data_find in line:
                return line[:line.find('\n')]
    log.save_log(file_path, f'Find_in_dbase: {data_find}')

# Удаление записи из базы данных
def del_row(file_path, file_format, data):
    my_list = []
    if file_format == 1: file_format = 'csv'
    elif file_format == 2: file_format = 'txt'
    
    with open(f'{file_path}\data\data.{file_format}', 'r', encoding = "utf_8") as file:
        my_list = file.readlines()
        result = ';'.join(data) + '\n'
        my_list.remove(result)
    with open(f'{file_path}\data\data.{file_format}', 'w', encoding = "utf_8") as file:
        file.write(''.join(my_list))
    log.save_log(file_path, f'Delete_from_dbase: {result[:-2]}')
    id_func.check_id(file_path, file_format)
    copy_dbase(file_path, file_format)

def copy_dbase(file_path, file_format):
    my_list = []
    if file_format == 1: file_format = 'csv'
    elif file_format == 2: file_format = 'txt'
    
    with open(f'{file_path}\data\data.{file_format}', 'r', encoding = "utf_8") as file:
        my_list = file.readlines()
    if file_format == 'csv': file_format = 'txt'
    elif file_format == 'txt': file_format = 'csv'
    
    with open(f'{file_path}\data\data.{file_format}', 'w', encoding = "utf_8") as file_2:
        file_2.write(''.join(my_list))
    log.save_log(file_path, f'Database_sync')
    