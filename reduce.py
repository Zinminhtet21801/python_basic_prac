from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def captitalize(name):
    return name.upper()


capitalized_names = map(captitalize, my_pets)
print(list(capitalized_names))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_over_50(score):
    return score > 50

over_50 = filter(is_over_50, scores)
print(list(over_50))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def add(acc, item):
    return acc + item


total = reduce(add, (my_numbers + scores))
print((my_numbers + scores))
