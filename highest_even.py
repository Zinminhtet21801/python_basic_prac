def highest_even(li):
    even_nums = []
    for num in li:
        if num % 2 == 0:
            even_nums.append(num)
    return max(even_nums)

print(highest_even([10, 2, 3, 4, 8, 11]))