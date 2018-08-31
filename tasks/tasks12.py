#12. Дан список значений. Превратить список в словарь поочередно превращая елменты в ключи и значения. [1, 2, 3, 4, 5, 6] -> {1: 2, 3: 4, 5: 6}
def dict_maker(values):
    made = {}
    index = 0
    for value in values[0::2]:
        made[value] = values[index + 1]
        index += 2
    return made


print(dict_maker([1, 2, 3, 4, 5, 6]))
