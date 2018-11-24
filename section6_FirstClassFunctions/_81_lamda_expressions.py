

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

















