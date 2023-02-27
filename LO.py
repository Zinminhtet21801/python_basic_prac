is_magician = bool(int(input('Are you a magician? (1/0): ')))


if not is_magician:
    print('You need magic powers') 
elif  is_magician:
    if bool(int(input('Are you a master magician? (1/0): '))):
        print('You are a master magician')
    else:
        print('At least you\'re getting there')