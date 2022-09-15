# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

import math

# Вычисление числа пи при помощи рядов Лейбница
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...

def calc_pi_Leibnic(accuracy: int) -> float:
    denom = 1
    count = 1
    result = 0
    for i in range(0, 1000000): #accuracy + 1
        if count % 2 == 0:
            result += (4 / denom) - (4 / (denom + 2))
        else:
            result += (4 / denom) - (4 / (denom + 2))
        count += 1
        denom += 4
    return int(result * accuracy) / accuracy

# Вычисление числа пи при помощи ряда Нилаканта
# π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...

def calc_pi_Nilakant(accuracy: int) -> float:
    denom = 1
    count = 0
    result = 3

    for i in range(0, 1000000):
        if count % 2 == 0:
            result += (4 / ((denom+1)*(denom+2)*(denom+3)))
        else:
            result -= (4 / ((denom+1)*(denom+2)*(denom+3)))
        count += 1
        denom += 2
    return int(result * accuracy) / accuracy

# Функция вычисления заданной точности

def calc_accur(input: str) -> int:
    result = input[input.find('.') + 1:]
    for i in range(len(result)):
        i += 1
    return 10 ** i

accur_input = input('Введите точность в формате 0.001: ')
accur_number = calc_accur(accur_input)

print(f'Вычисление при помощи рядов Лейбница: {calc_pi_Leibnic(calc_accur(accur_input))}')
print(f'Вычисление при помощи рядов Нилаканта: {calc_pi_Nilakant(calc_accur(accur_input))}')
print(f'Для проверки правильности расчета до точности {len(str(accur_number - 1))} знака/ов: {math.pi}')


