
def outer():
    x = "Python"
    y = 10
    def inner():
        print(y)
        print(x)
    return inner

fn = outer()
print("fn\'s free variables", fn.__code__.co_freevars)
print("fn\'s closures", fn.__closure__)

print('\n*** Beware of string interning, happens automatically ***')


def outer():
    x = [1, 2, 3]
    print("\touter x:{}", hex(id(x)))

    def inner():
        x = [1, 2, 3, 4]
        print("\tinner x:", hex(id(x)))
        print("\tinner x=", x)

    print("\touter x=", x)
    return inner

fn = outer()
fn()




print('\n*** Beware of string interning, happens automatically ***')
def outer():
    x = [1, 2, 3]
    print("\touter x = {} at: {}".format(x, hex(id(x))))

    def inner():
        y = x
        print("\tinner x = {} at: {}".format(y, hex(id(y))))
    return inner

fn = outer()
print(fn.__closure__)
fn()




print('\n*** Using a closure for incrementing ***')
def outer():
    count = 0

    def inc():
        nonlocal count
        count += 1
        print("\t", count)
        return count
    return inc

fn = outer()
print('\tGetting the closure info')
print(fn.__closure__)
print(fn.__code__.co_freevars)
print('\tPrinting the singleton 0 object, should be the same')
print(hex(id(0)))
fn()
print(fn.__closure__)
print(fn.__code__.co_freevars)



print('\n*** All nonlocals pointing to the same cell, which points to the variable ***')
def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 2
        return count

    return inc1, inc2

fn1, fn2 = outer()
print("\tfn1: {}".format(fn1.__code__.co_freevars))
print("\tfn2: {}".format(fn2.__code__.co_freevars))
print("\tfn1: {}".format(fn1.__closure__))
print("\tfn2: {}".format(fn2.__closure__))
print("result", fn1())
print("\tfn1: {}".format(fn1.__closure__))
print("result", fn2())
print("\tfn2: {}".format(fn2.__closure__))
print("result", fn1())
print("\tfn1: {}".format(fn1.__closure__))



print('\n***  Using closures for a power of function, a new scope every time ***')
def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)
print("\tsquare {}".format(square.__closure__))
cube = pow(3)
print("\tcube   {}".format(cube.__closure__))
print(square(5))
print(cube(5))



print('\n*** Inadvertently create closures ***')
print('\tdifferent cells for each add_n')
def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
print(add_1.__closure__)
add_2 = adder(2)
print(add_2.__closure__)
add_3 = adder(3)
print(add_3.__closure__)

adders = []
for n in range(1,4):
    # This global n is the same label in 3 different scopes
    # This isnt a closure buuut...
    adders.append(lambda x: x + n)

print(adders[0](10))



print('\n*** Avoiding creating a closure using default values ***')
print('\tThe value for n is looked up when you CALL the lambda ')
def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x: x + n)
    return adders

print('\tReference the samce cell every time, same n')
fn = create_adders()
print(fn[0].__closure__)
print(fn[1].__closure__)
print('\tBecause it\'s the same cell then all the fn use the SAME n')
print('\tThe SAME cell')
print(fn[0](10))



print('\n*** How to work properly, use different n\'s ***')
def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x, y=n: x + y)
    return adders

fn = create_adders()
print('\tAre these closures? NO, None')
print(fn[0].__closure__)
print(fn[1].__closure__)
print('\tDefault values are evaluated at creation time, so y will not point to the cell anymore')
print('\tThis is no longer a free variable')
print(fn[0](10))
print(fn[1](10))























