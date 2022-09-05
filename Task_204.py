# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input('Введите число N: '))
list_numbers = []
mult_list = []

for i in range(-n, n + 1):
    list_numbers.append(i)
print(list_numbers)

mult_numbers = input('Введите номера элементов списка для умножения через пробел: ')
mult_list = mult_numbers.split(' ')

# Ввожу -1 у значений индексов для удобства пользователя, при счете с 1
result = list_numbers[int(mult_list[0]) - 1] * list_numbers[int(mult_list[1]) - 1]

print(result)