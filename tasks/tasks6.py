#6. Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
def bigger_then_pred(values):
    number_that_bigger_then_pred = []
    for index, value in enumerate(values):
        if value > values[index - 1]:
            number_that_bigger_then_pred.append(value)
    return number_that_bigger_then_pred

print(bigger_then_pred([-1, -2, -1, -5,6, 7, 9, 2, 4]))