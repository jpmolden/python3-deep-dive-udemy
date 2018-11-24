

# Called anonymous functions

# lambda [param list (optional]: expression
# Returns a function object

lambda x: x**2
# Anonymous (There is no function name)
lambda x,y: x + y
lambda : "hello"
lambda s: s[::-1].upper()
# Lambdas are NOT closures!!!
# They can be but don't have to be

my_func = lambda x: x**2

# Same as
def my_func(x):
    return x**2

print(my_func(2))

print("\n*** Pass as an arg to another function ***")
def apply_func(x, fn):
    print("\tPassing x={}, result={}".format(x, fn(x)))
    return fn(x)

print('\tWork as inline functions, that are anonymous, they cannot be referenced by name')
apply_func(3, lambda x: x**2)
apply_func(3, lambda x=5: x**2)
apply_func(3, lambda x: x + 2)
apply_func('abc', lambda x: x[1:] * 3)


print('\tEquivilent to')
def fn_1(x):
    return x[1:] * 3

apply_func('abc', fn_1)

print("\n*** Limitations ***")
print('\tLimit to single expression')
print('\tNo assignment')
print('\tNO: lamda x: x + 5 NO')
print('\tNO: Annotations')


def sq(x):
    return x**2


print("sq is a: {}".format(type(sq)))

print((lambda x: x**2).__name__)
print((lambda x: x + y))



f = sq
print(id(f), id(sq))
print("f is reallt just: {}".format(f.__name__))

g = lambda x, y=10: x + y

print("g is :{}".format(g.__name__))
print('\tLambdas can be assigned and called')
print("\tResult of g(2,3) = {}".format(g(2,3)))


f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

print("\t", f(1, 'a', 'b', y=1, p=12, d=12))


print('\n*** Passing function to another function ***')
def apply_func(x, fn):
    return fn(x)


print("\t", apply_func(3, sq))
print('\tSame result through a lambda')
print('\tCreating a function on the fly')
print("\t", apply_func(3, lambda x: x**2))
print("\t", apply_func(3, lambda x: x**3))


def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

print("\t", apply_func(sq, 2))
print("\t", apply_func(lambda x, y: x + y, 1, 2))
print("\t", apply_func(lambda x, *, y: x + y, 1, y=2))
print("\t", apply_func(lambda *args: sum(args), 1,2,3,5,5,5,7))

print("\t", apply_func(apply_func(sum, (1,2,3,5,5,5,7)))








