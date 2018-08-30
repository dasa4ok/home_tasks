a = [1, 2, 3, 4, 5, 6, 7, 8]
index_of_the_number = 0
for i in a:
    if i % 2 != 0:
        a[index_of_the_number] = 0
    else:
        pass
    index_of_the_number += 1

print(a)