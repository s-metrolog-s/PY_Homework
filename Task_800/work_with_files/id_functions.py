from encodings import utf_8

# Генерация нового ID по последней записи в базе данных
def id_generator(file_path, file_format):
    my_list = []
    if file_format == 1: file_format = 'csv'
    elif file_format == 2: file_format = 'txt'
    
    with open(f'{file_path}\data\data.{file_format}', 'r', encoding = "utf_8") as file:
        my_list = file.readlines()
        result = my_list[-1]
    return str(int(result[:result.index(';')]) + 1)

# Нумерация всех записей в базе данных по порядку
def check_id(file_path, file_format):
    my_list = []
    if file_format == 1: file_format = 'csv'
    elif file_format == 2: file_format = 'txt'

    with open(f'{file_path}\data\data.{file_format}', 'r', encoding = 'utf-8') as file:
        my_list = file.readlines()
        count = 1
        for i in range(len(my_list)):
            work_space = my_list[i][:my_list[i].index(';')]
            my_list[i] = my_list[i].replace(str(work_space), str(count), 1)
            count += 1
    with open(f'{file_path}\data\data.{file_format}', 'w', encoding = 'utf-8') as file:
        file.write(''.join(my_list))