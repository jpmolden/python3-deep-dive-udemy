

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
    def inner():
        a = 10 # local variable
        print("{0} rocks!".format(x))
    return inner


fn = outer()
print("\tThe free vars", fn.__code__.co_freevars)
print("\tThe whats going on with the free variables", fn.__closure__)









