basket = [1,2,3,4,5 ]

basket.append(100)
basket.insert(4,99)
basket.extend([100,101])

for i in range(len(basket)):
    print(i)
print(list(range(100000000)))
print(1 in basket)

basket.reverse()
basket.sort()

print(basket)