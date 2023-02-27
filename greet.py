def hello():
    print("Hello, World!")


greet = hello
del hello
print(greet, hello)
