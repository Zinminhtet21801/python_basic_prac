while True:
    try:
        age = int(input('Enter your age: '))
        print('Your age is', age)
        raise ValueError('Invalid input for age') #throwing an exception
        # break
    except ValueError as e:
        print('Invalid input', e)
