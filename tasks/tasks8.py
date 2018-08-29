#8. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
def how_mutch_elem(values):
    counter = 0
    last_element = len(values) - 1
    elements = []
    for index, value in enumerate(values):
        if 0 < index < last_element:
            if values[index - 1] < value and values[index + 1] < value:
                counter += 1
    return counter

print(how_mutch_elem([-1, -2, -1, -5,6, 5, 9, 2, 4]))
