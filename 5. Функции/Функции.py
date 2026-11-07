# Функция, суммирующая числовой ряд от a до b

# Функция, возвращающая сумму ряда
def sum_sequence(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s

# Функция, печатающая числовой ряд на экран
def print_sequence(a, b):
    for i in range(a, b + 1):
        print(i, end=" ")
    print()


start = 12
finish = 25

print(sum_sequence(start, finish))
print_sequence(start, finish)