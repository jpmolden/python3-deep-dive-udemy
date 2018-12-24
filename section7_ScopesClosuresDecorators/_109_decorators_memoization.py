
print('Cache the values that have already been calculated')


def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print('\nCalculating recursively is inefficient in this example')
fib(10)


print('\n*** Calculate using caching instead ***')
class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        # look in cache
        if n not in self.cache:
            print("\tCalculating fib({0})".format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]


f = Fib()
f.fib(1)
f.fib(2)
f.fib(10)
f.fib(11)


print('\n*** Using a closure instead ***')


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        # Cache is a free variable
        if n not in cache:
            print("\tCalculating fib({0})".format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib


f = fib()
f(10)
f(11)

print('\tWith a new closure the calculations and cache must be done again')
g = fib()
g(10)



print('\n*** Using a decorator instead ***')
# This function either calculates new cache items / returns them
# It works with any single arg fn, late we'll see hashing techniques
def memoize(fn):
    cache = dict()

    def inner(n):
        # Cache is a free variable
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner


@memoize
def fib(n):
    print("\tCalculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print('\tSAME Behavior, the decorator changes the way the function operates')
print(fib(10))
print('\tThe next time its called it uses the cache, no new calculations needed')


@memoize
def fact(n):
    print("\tCalculating fact({0})".format(n))
    return 1 if n < 2 else n * fact(n-1)


print('\n*** Memoize the factorial function ***')
print(fact(10))
print('\tHere the fact(12) only needs to calculate 11! and 12 since the others are cached')
print(fact(12))

from time import perf_counter
start = perf_counter()
fib(20)
end = perf_counter()
print("Caching is FAR more efficient, took {:.6f}s".format(end - start))


print('\n*** Using the args tuple ***')
# def memoize(fn):
#     cache = dict()
#
#     def inner(*args):
#         # Cache is a free variable
#         if n not in cache:
#             cache[args] = fn(args)
#         return cache[n]
#     return inner

print('\tThis is more complex when using the *args, and **kwargs')
print('\tAnother potential problem is memory usage')
print('\tDicard? limit_items? recently_used?')

print('\n*** Least Recently Used Caching decorator ***')
print('\tThis is a parameterized decorator')
from functools import lru_cache

@lru_cache()
def fib(n):
    print("\tCalculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10)
fib(11)

print('\n*** Using a limited cache size ***')
print('\tlru_cache can limit cache size ect with parameters')
@lru_cache(maxsize=8)
def fib(n):
    print("\tCalculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print("fib({0}) = {1}".format(8, fib(8)))
print("fib({0}) = {1}".format(9, fib(9)))
print('\tHere the the fib(1) has fallen off the cache and needs to be recalculated')
print("fib({0}) = {1}".format(10, fib(10)))


