# 2. Найти сумму положительных элементов списка.
def counter(values):
    counter = 0
    for i in range(len(values)):
        if i > 0:
            counter += i
    return counter

print(counter([-1, -2, -5,6, 7, 9, 2, 4]))
