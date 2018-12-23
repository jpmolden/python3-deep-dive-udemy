
print('\nApplication of decorators (Timing)')
print('\tDecorators allow you to add other functionality to functions, using closures')


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        # List comprehension
        args_ = [str(a) for a in args]
        # List comp on iterable of tuples
        kwargs_ = ["{0}={1}".format(k, v) for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        # Big string of all arguments
        args_str = ",".join(all_args)

        print("\t{0}({1}) took {2:.6f}s to run".format(fn.__name__,
                                                       args_str,
                                                       elapsed))
        return result
    # Return closure
    return inner


# @timed
def fibonaci(n: int) -> int:
    #recursion
    if n <= 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

# fibonaci(6)

print('\n*** Getting the main function time ***')

@timed
def fib_recursive(n):
    return fibonaci(n)

# print(fib_recursive(50))


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2

print(fib_loop(50))

# n = 1
# (1,0) -> (1, 1) -> result is index[0]

# n = 2
# (1,0) -> (1, 1) -> (2, 1) -> result is index[0]

# n = 3
# (1,0) -> (1, 1) -> (2, 1) -> (3, 2) -> result is index[0]

# n = 4
# (1,0) -> (1, 1) -> (2, 1) -> (3, 2) -> (5, 3) -> result is index[0]

# previous val = (a  , b)
# new value    = (a+b, b)

from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0]+prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]

print(fib_reduce(50))

print('\tHere loop is FASTER!!!')



