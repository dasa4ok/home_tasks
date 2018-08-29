#4. В списке найти минимальный и максимальный элементы, поменять их местами.
def revers_of_min_and_max(values):
    maximum = max(values)
    minimum = min(values)
    for index, value in enumerate(values):
        if maximum == value:
            values[index] = minimum
        elif minimum == value:
            values[index] = maximum
    return values

print(revers_of_min_and_max([-1, -2, -5,6, 7, 9, 2, 4]))







