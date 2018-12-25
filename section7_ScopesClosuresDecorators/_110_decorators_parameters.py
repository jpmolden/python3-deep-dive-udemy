
print('\n*** Parameterized decorators ***')


def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print("\tRuntime: {0:0.6f}s".format(elapsed))
        return result
    return inner



def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)


@timed
def fib(n):
    return calc_fib_recurse(n)

print("Result {}".format(fib(20)))





print('\n*** Using the other way to decorate ***')

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib)
print("Result {}".format(fib(20)))
print("Result {}".format(fib(30)))





print('\n*** What if we want to parametrize the decorator? ***')
def ave_timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start

        print("\tAvg_Runtime: {0:0.6f}s".format(total_elapsed/10))
        return result
    return inner


print('\tFirst: Need to redefine fib because right now fib is the decorated fib')
print('\tOtherwise we will decorate twice')

def fib(n):
    return calc_fib_recurse(n)

fib = ave_timed(fib)
print("Result {}".format(fib(20)))





print('\n*** Making a parameterized decorator ***')
def ave_timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start

        print("\tAvg_Runtime: {0:0.6f}s for {1} reps".format(total_elapsed/reps, reps))
        return result
    return inner

def fib(n):
    return calc_fib_recurse(n)

print('\tThis works but will fail with the @ave_timed(5) syntax')
fib = ave_timed(fib, 5)
print("Result {}".format(fib(20)))






print('\n*** Making a decorator FACTORY, it makes decorators ***')
def dec(fn):
    print("running dec")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)

    return inner

print('\tThis syntax, with @')
@dec
def my_func():
    print("running my_func")

def my_func():
    print("running my_func")

print('\tIs the same as')
my_func = dec(my_func)
print('\tThe decorator is called')

my_func()


#
#
print('\n*** The decorator factory ***')
def dec_factory():
    print("\tRunning decorator factory")

    def dec(fn):
        print("\trunning dec")

        def inner(*args, **kwargs):
            print("\trunning inner")
            return fn(*args, **kwargs)

        return inner

    return dec


print('\tThe factory creates and returns the decorator that we want')
my_dec = dec_factory()

def my_func():
    print("running my_func")

print('\tThis syntax - Using the decorator from the decorator factory to decorate my_func')
my_func = my_dec(my_func)
my_func()

print('\tOR this syntax - Using the decorator to decorate my_func with the @ syntax')
@my_dec
def my_func():
    print("running my_func")

my_func()

print('\tOR this syntax - Calling the decorator factory to make a decorator for my_func')
@dec_factory()
def my_func():
    print("running my_func")

my_func()




print('\n*** dec_factory is a CALLABLE which creates a decorator ***')
print('\tEquivalently..')
def my_func():
    print("running my_func")

print('\tdec_factory creates the decorator which is applied to my_func')
my_func = dec_factory()(my_func)


print('\n*** Using a parameterized decorator factory ***')
def dec_factory(a, b):
    print("\tRunning decorator factory")

    def dec(fn):
        print("\trunning dec")

        def inner(*args, **kwargs):
            # Inner is a closure that contains a, b as free variables
            print("\trunning inner")
            print("\ta = {} b = {}".format(a, b))
            return fn(*args, **kwargs)

        return inner
    return dec

print('\tCalling the parameterized factory')
dec = dec_factory(10, 20)

@dec
def my_func():
    print("running my_func")

print('Now we run the function')
my_func()




print('\n*** Using the factory directly ***')

@dec_factory(100, 200)
def my_func():
    print("\tRunning {}".format("my_func"))

print('\n\tCalling the function')
my_func()

print('\n\tThis is the same as')
my_func = dec_factory(100, 256)(my_func)




print('\n*** Back to the timed example, creating a parameterized decorator ***')
def timed(n=10):
    def decorator(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(n):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start

            print("\tAvg_Runtime: {0:0.6f}s for {1} reps".format(total_elapsed/n, n))
            return result
        return inner
    return decorator

@timed(1)
def some_function(a, n):
    return a ** n

some_function(1, 5)

