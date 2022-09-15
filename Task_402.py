# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def simple_multiplier(input_number: int) -> list:
    result_list = []
    while input_number != 1:
        if input_number % 2 == 0:
            input_number /= 2
            result_list.append(2)
        elif input_number % 3 == 0:
            input_number /= 3
            result_list.append(3)
        elif input_number % 5 == 0:
            input_number /= 5
            result_list.append(5)
        elif input_number % 7 == 0:
            input_number /= 7
            result_list.append(7)
        else:
            result_list.append(int(input_number))
            break
    if len(result_list) == 1:
        result_list.insert(0, 1)
    return result_list

print('Разложим число на простые множители')
number = int(input('Введите число: '))
print(f'Список множителей числа {number} - {simple_multiplier(number)}')