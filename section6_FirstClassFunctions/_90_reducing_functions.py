
print('\n*** What are they ***')
print('\tThey are functions that recombine an iterable recursivly, ending up with a single return value')
print('\tAlso called accumulators, aggregators or folding functions')


print('\n*** Example: Find max value in an iterable ***')
print('\tMaps an iterable to a value')
print('\ta0, a1, a2... an-1')

print('\tmax(a, b)')
print('\tresult = a0')
print('\tresult = max(result, a1)')

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


max_val_f = lambda a,b: a if a > b else b
min_val_f = lambda a,b: a if a < b else b
add_val_f = lambda a,b: a + b

l = [5,8,6,10,9]
max_val = _reduce(max_val_f, l)
min_val = _reduce(min_val_f, l)
add_val = _reduce(add_val_f, l)

print(max_val)
print(min_val)
print(add_val)


print('\n*** Using the builtin reduce function ***')
print('\tThis works on ANY iterable not just sequences')
from functools import reduce
max_val = reduce(lambda a,b: a if a > b else b, l)
min_val = reduce(lambda a,b: a if a < b else b, l)
add_val = reduce(lambda a,b: a + b, l)
print(max_val)
print(min_val)
print(add_val)

st = "python"
min_val = reduce(lambda a,b: a if a < b else b, st)
print(min_val)

st_tup = ("python", "is", "Awesome!")
concat_val = reduce(lambda a,b: a + ' ' + b, st_tup)
print(concat_val)

print('\n*** Built in reducing functions for iterables ***')
print('\tmin, max, sum, any, all')
print('\tAny returns True if any element is Truthy')
print('\tAll returns True if all elements is Truthy')


print('\n*** Using reduce to reproduce any ***')
any_f = lambda x, y: bool(x) or bool(y)
l = [0, '', None, 0.0]
any_val = reduce(any_f, l)
print(any_val)


print('\n*** Using reduce to get product ***')
prod_f = lambda x,y: x * y
print('\tres = l[0]')
print('\tres = res * l[1]')
print('\tres = res * l[2]...')
l = [1,10,4,3.5,5,7]
prod_val = reduce(prod_f, l)
print(prod_val)


print('\n*** Calculate n! ***')
x = reduce(lambda a,b: a * b, range(1, 5+1))
print("5! =", x)


print('\n*** The intializer in reduce ***')
print('\tSets the initial value somthing other than the first iterable item/index')
l = []
min_with_intial = reduce(lambda x,y: x + y, l, 0)
print(min_with_intial)


