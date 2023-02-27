# my_list = []

# for char in 'hello':
#     my_list.append(char)

print(list('my_list'))
my_list = [num*2 for num in range(1, 101)]
# even_list = [num for num in range(1, 10000000)
#              if num % 2 == 0]

even_list = [num for num in range(0, 100, 2)]
print(even_list)
