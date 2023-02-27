from functools import reduce


def multiply_by2(item):
    return item*2


multiplied_list = map(multiply_by2, [1, 2, 3])
print(list(multiplied_list))


def isNotEven(item):
    return item % 2 != 0



not_even = filter(isNotEven, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(not_even))

nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',]

print(list(zip(nums_list, alphabets_list)))


def accumulator(acc, item):
    print(acc, item, 'acc + item = ', acc + item)
    return acc + item


reducedNums = reduce(accumulator, nums_list, 0)
print(reducedNums)
