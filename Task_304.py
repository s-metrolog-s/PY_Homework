# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# функция проверки ввода
def check_input_int(text: str) -> int:
    while True:
        number = input(f'{text}')
        if number.isdigit():
            break
    return int(number)

# функция конвертации
def convert_one_zero(number: int) -> str:
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    return result

number = check_input_int('Введите число: ')
print('Конвертируем в двоичную систему...')
print(f'Результат: {convert_one_zero(number)}')