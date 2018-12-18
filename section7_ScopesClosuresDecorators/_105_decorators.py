
print('\n*** A decorator ***')
print('\ttakes a function as an argument')
print('\treturns a closure')
print('\tthe closure usually accepts any number of combination of parameters')
print('\truns some code in the inner function(closure)')
print('\tthe closure calls the original function using the arguments passed to the closure')
print('\treturns whatever is returned by that function call')


print('\n*** The @ symbol ***')
print('\tfor convenience only can use closures')

def decorator_fn(fn):
    print("\tdecorating {}".format(fn.__name__))
    def inner_fn(*args, **kwargs):
        print("\tResult: {}".format(fn(*args, **kwargs)))
        return fn(*args, **kwargs)
    return inner_fn

def add(a, b):
    return a + b

add = decorator_fn(add)

add(1, 2)


print('\n*** In general, if func is a decorator function ***')
print('\twe decorate using: my_func = func(my_func)')
print('\tOr in a convenient way:....with')
'''
@counter
def add(a, b):
    return a + b
'''

'''
same as
def add(a, b):
    return a + b
    
add = counter(add)
'''

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{} was called {} times".format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

@counter
def mult(a, b, c=1):
    return a * b * c

print('\tMult now looks like inner because of the decorator function')
print('\tThink back to closures')
print('\tThe help and name no longer look the same, they are hidden in a free variable in the closure')
print(mult.__name__)
print(mult(1,2,3))


print('\n*** Getting the original signature back ***')
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{} was called {} times".format(fn.__name__, count))
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

@counter
def mult(a, b, c=1):
    return a * b * c

print(mult.__name__)
print(mult(1,2,3))


print('\n*** The wraps function, a decorator for copying metadata, name, docstring, ect. ***')
from functools import wraps
def counter(fn):
    count = 0
    '''@wraps(fn), same as wraps(fn)(inner)'''
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{} was called {} times".format(fn.__name__, count))
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner

@counter
def mult(a, b, c=1):
    return a * b * c



print('\n*** The wraps function, a decorator for copying metadata, name, docstring, ect. ***')
from functools import wraps
def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{} was called {} times".format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

@counter
def mult(a, b, c=1):
    """
        The product of 3 values
    """
    return a * b * c



