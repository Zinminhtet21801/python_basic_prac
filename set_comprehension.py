
# for char in 'hello':
#     my_list.append(char)

# print(set('my_list'))
# my_list = {char for char in 'hello'}
# print(my_list)
# my_list = [num*2 for num in range(1, 101)]
# # even_list = [num for num in range(1, 10000000)
# #              if num % 2 == 0]

# even_list = [num for num in range(0, 100, 2)]
# print(even_list)

my_dict = {key: value for key, value in {'a': 1, 'b': 2}.items()}
print(my_dict)

my_dict = {num: num**2 for num in [1, 2, 3]}
print(my_dict)
