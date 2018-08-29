#10. В одномерном списке удалить все четные элементы и оставить только нечетные.
def remover_of_even(values):
    for value in values[0:]:
        if value % 2 == 0:
            quantity = values.count(value)
            for elements in range(quantity):
                values.remove(value)
    return values

print(remover_of_even([-1, -2, -1, -5,6, 7,-1, 8, 6, 9, 9, 2, 4]))
