
def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        print(initial_value)
        return initial_value
    return inc

counter1 = counter()

counter1()
counter1()


def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("{0} has been call {1} times".format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)

counter_add(10, 30)

counter_mult = counter(mult)
counter_mult(10, 200)


print('\n*** Counting the number of function calls in a global dict ***')
counters = dict()
def countern(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        global counters
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

counted_add = countern(add)
counted_mul = countern(mult)
counted_add(10, 20)
counted_mul(10, 20)
counted_add(10, 20)

print(counters)


print('\n*** Passing in the counters dict ***')
def countern(fn, counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

c = dict()
counted_add = countern(add, c)
counted_mul = countern(mult, c)
counted_add(10, 20)
counted_mul(10, 2)
print(c)


print('\n*** A Factorial Function ***')
def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

counted_fact = countern(fact, c)
print(counted_fact(5))
print(c)
fact = countern(fact, c)
print('\tFact is now a closure')
print(fact.__closure__)
print(fact.__code__.co_freevars)
print('\tModifying the function with a closure, does the function plus some extra bits')
print('\tHere we are decoratoing the function add with the funciton counter')
add = countern(add, c)
mult = countern(mult, c)
add(10,20)
add(10,20)
mult(10,2)
print(c)



