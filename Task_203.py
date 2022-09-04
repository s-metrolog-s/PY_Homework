# Задайте список из k чисел последовательности (1 + 1/k)^k и выведите на экран их сумму.

k = int(input('Введите число K: '))

list_numbers = []
sum = 0

for i in range(1, k + 1):
    result = round((1 + 1/i)**i, 2)
    sum += result
    list_numbers.append(result)

print(f'Сумма последовательности {list_numbers} равна {sum}')