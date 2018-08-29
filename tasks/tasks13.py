#13. Дано два списка значений, вывести значения которые есть в обоих списках [1,2,3,4] [3, 5, 7, 1] -> [1, 3]
def finder_of_same(values1, values2):
    counter = []
    for value1 in values1:
        if values2.count(value1) >= 1:
            counter.append(value1)
    return counter

print(finder_of_same([1,2,3,4], [3, 5, 7, 1]))



