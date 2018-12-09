

print('*** Using non local variables ***')
print('\tPython looks in an enclosing scope')
def outer_func():
    x = "Hello"

    def inner_func():
        print(x)

    inner_func()

outer_func()


print('\n*** Using functions within functions ***')
print('\tinner 2 looks into inner1 then outer_func, untill it finds x')
def outer_func():
    x = "Hello"

    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

outer_func()


print('\n*** Assignment creates a local scope ***')
print('\tWhen inner was created (not exec) python sees an assignment to x, and says it is a local variable')
print('\t*** The inner x masks the outer x, ie it does not change ***')
def outer_func():
    x = "Hello"

    def inner():
        x = "Python"
        print("inner x:", x)

    inner()
    print("outer x:", x)

outer_func()


print('\n*** Using assingment with nonlocal scope  ***')
x = "Global"
print("global x:", x)

def outer_func():
    x = "Hello"

    def inner():
        nonlocal x
        x = "Python"
        print("inner x:", x)

    print("outer (before) x:", x)
    inner()
    print("outer (after) x:", x)

outer_func()
print("global x:", x)



print('\n*** Using nesting with nonlocal scope  ***')
x = "Global"
print("global x:", x)

def outer_func():
    x = "Hello"
    print("outer (before) x:", x)
    def inner1():
        def inner2():
            nonlocal x
            x = "Python"
        inner2()
    inner1()
    print("outer (after) x:", x)

outer_func()
print("global x:", x)


print('\n*** Using global keyword  ***')
x = "Global"
print("global x:", x)

def outer_func():
    global x
    x = "outer"

    def inner():
        # Remove the nonlocal or an no binding error will occur
        # nonlocal x
        global x
        x = "inner"
        print("inner x", x)

print('\tHere x does not belong to outer_funcs local scope and so it will cause an error when inner tries to assign')
print('\tThis causes a Syntax error: no binding')

outer_func()
print("global x:", x)









