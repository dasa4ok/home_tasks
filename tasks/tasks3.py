#3. Дан список, содержащий положительные и отрицательные числа. Заменить все элементы списка на противоположные по знаку. Например, задан список [1, -5, 0, 3, -4]. После преобразования должно получиться [-1, 5, 0, -3, 4].
def func(values):
    for index, value in enumerate(values):
        if value > 0:
            something = 0
            something = value - (value * 2)
            values[index] = something
        elif value < 0:
            something = 0
            something = value + (value * (-2))
            values[index] = something
        else:
            pass
    return values

print(func([-1, -2, -5,6, 7, 9, 2, 4]))
