#11. Дан список значений. Превратить список в словарь где ключами служат элементы списка, а значениями квадраты этих элементов. [1,2,3] -> {1:1, 2:4, 3:9}
def dict_maker_of_square(values):
    dict_of_square = {}
    for value in values:
        dict_of_square[value] = value ** 2
    return dict_of_square

print(dict_maker_of_square([1,2,3]))