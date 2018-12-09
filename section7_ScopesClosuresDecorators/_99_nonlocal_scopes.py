
def outer_func():
    # Some code
    # a = 10

    def inner_func():
        print("Inner_func, non-local a = {}".format((a)))
        # some code

    inner_func()



print('*** Inner func is nested inside the outer func ***')
print('\tnon local scope - Inner func has access to the outer func scope')
a = 20
outer_func()


print('*** Modifying non-local variables ***')

def outer():
    x = "Hello"
    def inner1():
        x = "Python"
        def inner2():
            nonlocal x
            x = "monty"

        print("inner1 x:", x)
        inner2()
        print("call inner2")
        print("inner1 x:", x)

    inner1()
    print("outer x:", x)

outer()

print('\n*** Adding non locality to x in inner 1 ***')

x = "Global x"
print(x)
def outer():
    x = "Hello"
    def inner1():
        nonlocal x
        x = "Python"
        def inner2():
            nonlocal x
            x = "monty"

        print("inner1 x:", x)
        inner2()
        print("call inner2")
        print("inner1 x:", x)

    inner1()
    print("outer x:", x)

outer()
print(x)

print('\n*** Mixing nonlocal and global variables ***')
x = 100
print("Global x:", x)

def outer():
    x = "Python"
    def inner1():
        nonlocal x
        x = "Monty"
        def inner2():
            global x
            x = "hello"

        print("inner1 x:", x)
        inner2()
        print("call inner2()")
        print("inner1 x:", x)

    inner1()
    print("outer x:", x)

outer()
print("Global x:", x)








