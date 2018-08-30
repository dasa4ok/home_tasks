def print_list(x: list):
    for i in range(len(x)):
        print('-' * 10)
        print('|', ' '.join([str(i) for i in x[i]]), '|')

print(print_list([[125, 343, 123], [121, 450, 678]]))