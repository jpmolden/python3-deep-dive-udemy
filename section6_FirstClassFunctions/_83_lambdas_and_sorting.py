

print(sorted([1,7,3,4,5]))

l = [1,5,4,7,10,5,9]

print(sorted(l))
print(l)

l2 = ['c', 'b', 'a', 'A', 'B']

print('\n\tIllustrating the key kwarg')
print(sorted(l2))
print(l2)

print('\n\tGetting ascii table equililents')
print("\t", ord('a'))
print("\t", ord('A'))
print("\tIn ascii CAPS letters precede the lowercase")

print('\n*** Using lambdas for a case insensitive sort ***')
print(sorted(l2, key=lambda s: s.upper()))


print('\n***Using Lambdas for a value sort ***')
d = {"def": 3, "abc": 2, "ghi": 1}
for k in d:
    print("\t", k, d[k])

print("\tDict sorted by value not key:", sorted(d, key=lambda e: d[e]))


print('\n***Using Lambdas with complex numbers ***')
def dist_sq(x):
    return (x.real)**2 + (x.imag)**2


print("\t", dist_sq(1+1j))
l = [3+3j, 1-1j, 0, 3+0j]
print('\tSorting by euclidean distance:')
print("\t", sorted(l, key=dist_sq))
print('\tSame sort using lambdas')
print("\t", sorted(l, key=lambda num: (num.real)**2 + (num.imag)**2))


print('\n***Using Lambdas to do a sort by last character ***')
l = ["a", "ZZXXDDWWa", "ZZZZZe", "Potato", "AAAAe", "Happy", "Milk"]
def last_element(x):
    print("x[-1] = {}, x[0:-1] = {}, sortKey = {}".format(x[-1], x[0:-1], x[-1] + x[0:-1]))
    return x[-1]


print("\t", sorted(l, key=last_element))
print('\tSame thing using Lambdas')
print("\t", sorted(l, key=lambda s: s[-1]))
# Using a sort based on the entire string with last char taking precidence
print("\t", sorted(l, key=lambda s: s[-1] + s[0:-1]))











