import random
def gen_list0(n):
    new_list = []
    for i in range(n):
        new_list.append(random.randint(100, 999))
    return new_list
def gen_list(n):
    new_list = []
    for i in range(n):
        new_list.append(gen_list0(n))
    return new_list


print(gen_list(4))