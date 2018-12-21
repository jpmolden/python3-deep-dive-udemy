from functools import wraps

def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function {}:{} was called {} times".format(fn.__name__, id(fn), count))
        # *args and kwargs are not free variables
        result = fn(*args, **kwargs)
        print("\tresult {}", result)
        return fn(*args, **kwargs)
    return inner

def add(a:int, b:int = 0):
    """
    :param a:
    :param b:
    :return:
    Adds two values
    """
    return a + b

print('\n*** Using closures ***')
print('\tadd is now a new closure function, not the same function anymore')
print("Before assignment as a closure function:", add.__doc__)
print("id add", id(add))
add = counter(add)
print("After assignment as a closure function:", add.__doc__)
print("id add", id(add))
add(10, 20)
add(10, 20)
print('\tThe closure has a different memory address')


def mult(a:int, b:int, c:int = 1, *, d):
    """
    :param a:
    :param b:
    :param c:
    :return:
    Multiply 3 values
    """
    return a * b * c * d


mult(1,2,d=3)
mult = counter(mult)
mult(1,2,3, d=4)
mult(1,2, d=4)

print('\tHere mult has been decorated by counter')



print('\nThe easier way with @, decorator syntax (same as a closure)')
@counter
def my_func(s:str, i:int) -> str:
    """
    Repeats a string i times
    """
    return s * i

my_func("abd", 10)
print("With the wrap the function doc is back to:", my_func.__doc__)



def counter(fn):
    count = 0

    # @wraps(fn)   either or..
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function {}:{} was called {} times".format(fn.__name__, id(fn), count))
        # *args and kwargs are not free variables
        result = fn(*args, **kwargs)
        print("\tresult {}", result)
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner



print('\nUsing the alternative wraps syntax to also fix up the function metadata')
@counter
def my_func(s:str, i:int) -> str:
    """
    Repeats a string i times
    """
    return s * i

my_func("abd", 10)
print("With the wrap the function doc is back to:", my_func.__doc__)











