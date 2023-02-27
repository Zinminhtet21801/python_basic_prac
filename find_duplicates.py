some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
print(some_list)
my_set_list = {value for value in some_list if some_list.count(value) > 1}

print(list(my_set_list))
