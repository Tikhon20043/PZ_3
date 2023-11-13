def find_different_number(a, b, c, d):
    if a == b == c:
        return 4
    elif a == b == d:
        return 3
    elif a == c == d:
        return 2
    else:
        return 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвертое число: "))

result = find_different_number(a, b, c, d)
print("Порядковый номер числа, отличного от остальных:", result)
