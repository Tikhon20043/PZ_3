#Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника.
#Проверить истинность высказывания: «Треугольник со сторонами a, b, c является
#равносторонним»

a, b, c = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")

while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")
while type(b) != int: # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")
while type(c) != int: # обработка исключений
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите третье число: ")





if a == b and b == c:
    print("Треугольник является равносторонним")
else:
    print("Треугольник не является равносторонним")
