# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def make_rle(input_string: str) -> str:
    out_string = ''
    count = 1
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            count += 1
        else: 
            out_string += input_string[i] + str(count)
            count = 1
        if i == (len(input_string) - 2):
            out_string += input_string[i] + str(count)
    return out_string

def read_rle(input_string: str) -> str:
    out_string = ''
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            count = int(input_string[i])
            while count > 1:
                out_string += out_string[-1]
                count -= 1
        else:
            out_string += input_string[i]
    return out_string

input_string = 'aaababbcbbbqq'
reinput_string = 'a3b1a1b2c1b3q2'

print(f'Дана строка: {input_string}')
print('Преобразуем...')
print(make_rle(input_string))
print('-----------------------------------')
print(f'Дана строка: {reinput_string}')
print('Расшифруем...')
print(read_rle(reinput_string))
    
