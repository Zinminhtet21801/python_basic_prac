def listFib(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]


# print(listFib(2000))

def gen_fib(n):
    a = 0
    b = 1
    for _ in range(n+1):
        yield a
        a, b = b, a+b


for x in gen_fib(10):
    # print(x)
    pass
