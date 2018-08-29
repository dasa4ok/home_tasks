# 1. Найти номер и значение первого положительного элемента списка.
def first(values):
    for i, index in enumerate(values):
        if index > 0:
             return i, index

print(first([-2, -7, -71, 3, 4, 5, 6, ]))
