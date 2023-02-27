import crypt
import mimetypes

print(mimetypes.guess_type('password_checker.py'))

username = input('Enter your username: ')
password = input('Enter your password: ')

password_length = len(password)
starred_password = '*' * password_length
crypted_password = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

print(f'{username}, your password {starred_password} is {password_length} letters long. And here\'s your encrypted password: {crypted_password}')