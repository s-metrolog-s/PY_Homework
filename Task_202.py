# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N: '))

list_numbers = []
for i in range(1, n + 1):
    result = 1
    for k in range(1, i + 1):
        result *= k
    list_numbers.append(result)

print(list_numbers)