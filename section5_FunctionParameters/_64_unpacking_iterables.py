

print('\tSide Note - Tuple defined by the commas!! (1, 2, 3)')
single_tuple = (1,)
single_tuple = 1,

print(type(single_tuple))

print('\n*** Packed Values ***')
print('\tAny iterable is considered a packed value')
# t = (1,2,3)
# l = [1,2,3)
# s = 'Python'
# set1 = {1,2,3}
# d = {'a': 1, 'b': 2, 'c': 3}


print("\tUnpacking is splitting packed values into individual variables")
print('\tBoth sides are a tuple')
print('\ta, b, c = [1, 2, 3]')
a, b, c = "XYZ"

print('\n*** Application of unpacking ***')
print('\tSwapping Variables')
a = 10
b = 20
print("\ta={} b={}".format(a,b))
a, b = b, a
print("\ta={} b={}".format(a,b))

print('\tUnpacking sets and dics - Unordered Types')
# d = {"key1": 1, "key2": 2, "key3": 3}
s = {'a', 'b','c', 'd'}
a, b, c, d = s
print("\tSets are not ordered!!!!", a, b, c, d)















