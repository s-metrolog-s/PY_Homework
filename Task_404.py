# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def polynomial_generate(k: int) -> str:
    output_string = ''
    indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }
    
    for i in range(2):
        ran_number = randint(0, 100)
        if ran_number == 0:
            continue
        if ran_number == 1:
            output_string += f'x{indexes.get(str(k), 0)}'
        else:
            output_string += f'{ran_number}*x{indexes.get(str(k), 0)}'
        
        k -= 1
        output_string += ' + '

    ran_number = randint(0, 100)
    if k == 0:
        output_string += f'{ran_number} = 0'
    elif k == 1:
        output_string += f'{ran_number}*x = 0'
    else:
        output_string += f'{ran_number}*x{indexes.get(str(k), 0)} = 0'
           
    return output_string

k = int(input())
print(polynomial_generate(k))

with open('Task_404.txt', 'w', encoding = "utf-8") as f:
    f.write(polynomial_generate(k))

