import datetime
import crypt

name = 'Zin Min Htet'
age = 30
relationship_status = 'single'

birth_year = int(input('Enter your birth year: '))
print(datetime.datetime.now().year - birth_year)

password = input('Enter your password: ')

crypto = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

print(type(crypto), crypto)
