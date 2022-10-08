# Запись и чтение из базы данных

from encodings import utf_8

def add_row(file_path, file_format, data):
    if file_format == 1:
        with open(f'{file_path}\data.csv', 'a', encoding = "utf_8") as file:
            file.write(';'.join(data) + '\n')
    elif file_format == 2:
        with open(f'{file_path}\data.txt', 'a', encoding = "utf_8") as file:
            file.write(';'.join(data) + '\n')

def find_string(file_path, file_format, data_find):
    if file_format == 1:
        with open(f'{file_path}\data.csv', 'r', encoding = "utf_8") as file:
            for line in file:
                if data_find in line:
                    return line[:line.find('\n')]
 
    elif file_format == 2:
        with open(f'{file_path}\data.txt', 'r', encoding = "utf_8") as file:
            for line in file:
                if data_find in line:
                    return line[:line.find('\n')]

def del_row(file_path, file_format, data):
    my_list = []
    if file_format == 1:
        with open(f'{file_path}\data.csv', 'r', encoding = "utf_8") as file:
            my_list = file.readlines()
        result = ';'.join(data) + '\n'
        my_list.remove(result)
        with open(f'{file_path}\data.csv', 'w', encoding = "utf_8") as file:
            file.write(''.join(my_list))
                
    elif file_format == 2:
        with open(f'{file_path}\data.txt', 'r', encoding = "utf_8") as file:
            my_list = file.readlines()
        result = ';'.join(data) + '\n'
        my_list.remove(result)
        with open(f'{file_path}\data.csv', 'w', encoding = "utf_8") as file:
            file.write(''.join(my_list))
    pass