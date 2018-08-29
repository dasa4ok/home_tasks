#7. Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
def two_adjacent_of_one_sing(values):
    for index, value in enumerate(values[1:]):
        index += 1
        if len(values) < 2:
            return None
        else:
            if values[index - 1] > 0 and value > 0:
                return values[index - 1], value
            elif values[index - 1] < 0 and value < 0:
                return values[index - 1], value
            else:
                return None

print(two_adjacent_of_one_sing([-1, -2, -1, -5,6, 7, 9, 2, 4]))
