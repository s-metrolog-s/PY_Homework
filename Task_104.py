# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите четверть: '))

match quarter:
    case 1: 
        print("Точка лежит в пределах, где X > 0; Y > 0")
    case 2:
        print("Точка лежит в пределах, где X < 0; Y > 0")
    case 3:
        print("Точка лежит в пределах, где X < 0; Y < 0")
    case 4:
        print("Точка лежит в пределах, где X > 0; Y < 0")