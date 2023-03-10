# Scope - what variables do I have access to?
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

        def innerInner():
            nonlocal x
            x = "nonlocal innerInner"
            print("innerInner:", x)
        innerInner()
    inner()
    print("outer:", x)


outer()

# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - built in python functions
