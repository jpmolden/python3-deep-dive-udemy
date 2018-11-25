

l = [5,8,6,10,9]
_max = lambda x,y: x if x > y else y

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

_min = lambda x,y: x if x < y else y

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


from functools import reduce

# Create a set
s1 = {1,2,3,4,5,0.1}
print(reduce(_max, s1))

print('\n*** Built in reduction functions ***')
print('\tmin, max, sum, any, all')
s = {True, 1, 0, None}
print("\tAre they all Truthy, all(s) = {}".format(all(s)))
print("\tAre any Truthy,      any(s) = {}".format(any(s)))



print('\n*** Making our own all reducing function ***')
s = {True, 1, 0, None}
s = {True, 1, "d", 1.0}
result = reduce(lambda x,y: bool(x) and bool(y), s)
print(result)



print('\n*** Making our own any reducing function ***')
s = {True, 1, 0, None}
result = reduce(lambda x,y: bool(x) or bool(y), s)
print(result)


print('\n*** Making our own all false reducing function ***')
s = {False, 0, 0.0, None, "", 0+0j}
result = reduce(lambda x,y: bool(x) and (not(bool(y))), s, True)
print(result)


print('\n*** Making our own product reducing function ***')
s = {1,7,-1,5,0.5,3.14,5,1+2j}
result = reduce(lambda x,y: x * y, s)
print(result)


print('\n*** Making our own factorial reducing function ***')
result = reduce(lambda x,y: x * y, range(1, 10+1))
print(result)


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n+1))

print(fact(7))












