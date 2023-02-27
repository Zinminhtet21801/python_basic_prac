my_tuple = (1,2,3,4,5)
name_tuple = 'Zin', 'Min', my_tuple
print(5 in my_tuple)

print(my_tuple)
print(name_tuple)

my_list_with_redundant_numbers = [1,2,3,4, 4,  ]
my_list_without_redundant_numbers = set(my_list_with_redundant_numbers)
print(my_list_without_redundant_numbers)

is_old = True

if not is_old:
    print('You are not old')

result = ''
result = 'You are old' if is_old else 'You are not old'

print(result)