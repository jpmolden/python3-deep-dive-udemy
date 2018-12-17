

def outer():
    x = "Python"
    def inner():
        print("{0} rocks!".format(x))

    return inner

print('*** Returning a a closure ***')
print('\tx is a free variable in inner, it is bound to the outer variable x')
print('\tThis binding happens when outer runs and inner is created(but no exec yet), this is a closure\n')


fn = outer()
print('\tThe value of is retained even though the scope of outer is gone!')
fn()

print('\n*** Python cells and multi-scoped variables ***')
def outer(x):
    x = x
    def inner():
        # Here x is in 2 different scopes
        print(x)
    return inner

fn = outer(12)
fn()

print('\tPython creates a cell as an intermediary object')
print('\tA cell allows an indirect reference')
print('\tInner x still points to the same cell')

print('\n*** What is a closure ***')
print('\t it is the function plus the extended scope that contains the free variable')


def outer():
    a = 100
    x = "Python"
    print("\tIndirect reference to x:", hex(id(x)))
    def inner():
        a = 10 # local variable
        print("{0} rocks!".format(x))
    return inner


fn = outer()
print("\tThe free vars", fn.__code__.co_freevars)
print("\tThe whats going on with the free variables", fn.__closure__)

print('\n*** Modifying free variables ***')
def counter():
    count = 0

    def inc():
        print('\tCount is a free variable it is bound to the cell count')
        nonlocal count
        count += 1
        print("\tcount = {}".format(count))
        return count
    return inc


print('\tfn is a closure')
fn = counter()
fn()
fn()
fn()
fn()


print('\n*** Multiple instances of closures ***')
print('\tEach run of function a new scope is created, if that func generates a closure a new closure is created too')

f1 = counter()
f2 = counter()

print('\tThere two closures do not have the same scope')

f1()
f1()
f1()

f2()

print("\tf1 closure", f1.__closure__)
print("\tf2 closure", f2.__closure__)


print('\n*** Shared extended scopes ***')
def outer():
    count = 0

    # Count is a free variable
    def inc1():
        nonlocal count
        count += 1
        print("\tcount = {}".format(count))
        return count

    # This count points to same cell
    def inc2():
        nonlocal count
        count += 1
        print("\tcount = {}".format(count))
        return count

    return inc1, inc2

print('\tThe closure is created when the function is created')
f1, f2 = outer()
f1()
f2()
f1()



print('\n*** Shared extended scope can happen by MISTAKE ***')
def adder(n):
    def inner(x):
        print("\tresult {} + {} = {}".format(x, n, x + n))
        return x + n

    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

add_1(1)
add_2(1)
add_3(1)

print('\tSuppose we tried')
adders = []
for n in range(1, 4):
    # Still the same label n
    # Closures only happen with a free variable
    # A cell is created for n, SAME cell in the loop
    adders.append(lambda x: x + n)

for i, f in enumerate(adders):
    print("\t Adders {} = ".format(i), f(1))

print('\tWhy!!? All the n\'s point to the SAME cell')



print('\n*** Nested closures ***')
def incrementer(n):
    # inner + n is a closure
    def inner(start):
        current = start
        # inc + current + n is a closure
        def inc():
            # free variable
            nonlocal current
            current += n
            return current
        return inc
    return inner

fn = incrementer(2)
print("\tFree vars {}".format(fn.__code__.co_freevars))
inc_2 = fn(100)
print("\tFree vars {}".format(inc_2.__code__.co_freevars))
print(inc_2())
print(inc_2())

















