# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

with open('PY_Homework\Task_501(in).txt', 'r', encoding = 'utf-8') as f1:
    input_string = f1.read().split(' ')

with open('PY_Homework\Task_501(con).txt', 'r', encoding = 'utf-8') as f2:
    remove_letters = f2.read()

print(input_string)

res = [word for word in input_string if remove_letters not in word]

print(' '.join(res))

with open('PY_Homework\Task_501(res).txt', 'w', encoding = 'utf-8') as f3:
    f3.write(' '.join(res))