# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def find_old_cat(*args):
    ages = []
    for age in args:
        ages.append(age.age)
    return f'The oldest cat is {max(ages)} years old.'

cat1 = Cat('Zin', 3)
cat2 = Cat('Zain', 2)
cat3 = Cat('Zein', 5)

print(find_old_cat(cat1, cat2, cat3))
# 1 Instantiate the Cat object with 3 cats


# 2 Create a function that finds the oldest cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
