list_for_chenging = [1, -2, 5, 6, -7, 8, 23, -4, 0]
new_list = list()
for number in list_for_chenging:
    if number >= 0:
        new_list.append(number)
    elif number < 0:
        new_list.pop(number)
        new_list.insert()
        
print(list_for_chenging)
print(new_list)