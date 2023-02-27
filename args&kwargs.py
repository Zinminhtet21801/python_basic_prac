def super_func(*args, **kwargs):
    # print(kwargs.values())
    for i in kwargs.values():
        print(i)
    print(args[2])

super_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name='Jose', location='UK')