#9. Из одномерного списка удалить все повторяющиеся элементы (дубликаты) так, чтобы каждое значение встречалось в списке только один раз.
def remover_of_repetitive(values):
    for value in values:
        if values.count(value) > 1:
            quantity = values.count(value) - 1
            for elements in range(quantity):
                values.remove(value)
    return values

print(remover_of_repetitive([-1, -2, -1, -5,6, 7,-1, 8, 6, 9, 9, 2, 4]))