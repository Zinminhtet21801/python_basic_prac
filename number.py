# print(round(3.141592653589793, 2))  
# print(max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(abs(-10))
# print(pow(2, 3))
# print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(min(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

a = {
    'name': 'John',
    'age': 30,
}
b = a
b = {
    'name': 'Zin',
    'age': 30,
}

print(id(a), id(b), id(a))

# for i in range(1, 100000000000000000000000000000000000000):
#     print(i)