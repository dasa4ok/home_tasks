#5. Найти сумму и произведение элементов одномерного числового списка.
def sum_and_milt(values):
    sum = values[0]
    mult = values[0]
    for index, value in enumerate(values[:-1]):
        mult = mult * values[index + 1]
        sum = sum + values[index + 1]
    return sum, mult

print(sum_and_milt([-1, -2, -5,6, 7, 9, 2, 4]))