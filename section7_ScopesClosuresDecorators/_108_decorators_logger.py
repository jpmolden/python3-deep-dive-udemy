
print('\n*** Using decorators for a logging decorator ***')

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("\t{0}: called {1}".format(run_dt, fn.__name__))
        return result

    return inner


def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print("\t{0} ran for {1:.6f}s".format(fn.__name__, end-start))
        return result
    return inner


@logged
def func_1():
    pass


@logged
def func_2():
    pass


@logged
def func_3():
    pass


print('\n*** Stacking decorators ***')
# Log is called first, may look reversed
@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))

print(fact(10))


def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))

print('\tUsing a closure syntax, is equivilent')
fact = logged(timed(fact))
fact(10)



def dec_1(fn):
    def inner(*args, **kwargs):
        print("Running dec_1")
        return fn()
    # return the closure (inner plus the fn free variable)
    return inner



def dec_2(fn):
    def inner(*args, **kwargs):
        print("Running dec_2")
        return fn()
    # return the closure (inner plus the fn free variable)
    return inner


print('\n*** More stacked decorators ***')
@dec_1
@dec_2
def my_func():
    print("Running my_func")

# SAME as: my_func = dec_1(dec_2(my_func))
# dec_1 runs first

my_func()

print('*** Ordering of stacked decorators can and does matter ***')
print('\te.g save_resource = logged(auth(save_resource))')



