a = [5, 7, 8, 3, 4, 6, 8]
calc = 0
click = 2
for i in a:
    if i % 2 == 0 and click > 0:
        click -= 1
        calc += i
print(calc)

