
print('\tHigher order functions takes a function as a param and/or returns a function')
print('\tE.g sorted(.., key=some_func), map, filter')
print('\tOther alternatives to map, filter -> list comprehensions, generator expressions')



print('\n*** The map function ***')
print('\tmap(func, *iterables)')
print('\tReturns an iterator that calculates the function applied to each element of the iterables')
print('\tThe number of iterables is arbitrary and the map will finish at the end of the shortest iterable')
print('\t(if unequal length)')

l = [2,3,4]
def sq(x):
    return x**2

mapped_list = list(map(sq, l))
print(mapped_list)

l1 = [1,2,3]
l2 = [10,20,30]
def add(x,y):
    return x + y

map_with_2args = list(map(add, l1, l2))
print(map_with_2args)

print('\n*** Using lambda with map ***')
map_2args_lamda = list(map(lambda a, b: a + b, l1, l2))
print(map_2args_lamda)



print('\n*** The filter function ***')
print('\tThe same as map except only takes one iterable')
print('\tDecides whether or not to throw out items in the iterable')
print('\tfilter(func, iterable)')
print('\treturns: an iterator')
print('\tIf func is None it returns the truthy items in the iterable')
l = [0,1,2,3,4,5,6]
print(list(filter(None, l)))
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, l)))



print('\n*** The zip function ***')
print('\tTakes multiple iterables and returns one iterable of tuples')
print('\tStops at the shortest one')
print(list(zip([1,2,3,4], [10,20,30,40])))
print(list(zip([1,2,3,4,5], [10,20,30,40])))
print(list(zip([1,2,3,4,5], [10,20,30,40], ['a','b','c'])))
print(list(zip([1,2,3,4,5], [10,20,30,40], ['d','e'])))

l1 = [1,2,3]
l2 = [10,20,30,40]
l3 = 'python'
print(list(zip(l1,l2,l3)))
l1 = 'string I want to index'
l2 = range(l1.__sizeof__())
print(list(zip(l1,l2)))



print('\n*** List comprehension alternative to map ***')
l = [2,3,4]
def sq(x):
    return x**2

print("The map approach:", list(map(sq, l)))

print('\tThe for loop approach')
result = []
for x in l:
    result.append(x**2)

print("The for loop approach", result)

print('\tThe list comprehension approach')
result = [x**2 for x in l]
print("This list comprehension approach", result)

l1 = [1,2,3]
l2 = [10,20,30]
print(list(map(lambda x,y: x + y, l1, l2)))




print('\n*** Using zip with list comprehensions ***')
result = [x + y for x, y in zip(l1, l2)]
print("Zip and list comprehension:", result)



print("\n*** Filter and lambdas ***")
l = [1,2,3,4]
print(list(filter(lambda n: n % 2 == 0, l)))



print('\n*** Using filter and list comprehensions ***')
# return x for x in l IF x is even
result = [x for x in l if x % 2 == 0]
print(result)


print("\n*** Combining map and filter ***")
l = range(10)
# Square all elements in range 10 and only keep the elments < 25
print('\tUsing filter and map directly')
x = list(filter(lambda y: y < 25, map(lambda x: x**2, l)))
print(x)
print('\tUsing list comprehensions')
x = [x**2 for x in range(10) if x**2 < 25]
print(x)




#
# class MyClass:
#     def __init__(self, a):
#         self.a = a
#
#     def __bool__(self):
#         if self.a == 'Fail':
#             return False
#         else:
#             return True
#
#
# abc = MyClass('Pass')
# hij = MyClass('Fail')
#
# import inspect
#
# print("abc = {}, hij = {}".format(abc.__bool__(), hij.__bool__()))
#
# this_test = hij
# if this_test:
#     print("Object is Pass {}".format(inspect.signature(this_test)))
# else:
#     print("Object is Fail {}".format(inspect.signature(this_test)))
#
