

from functools import partial

def func(a,b,c):
    print(a,b,c)


f = lambda b,c: func(10,b,c)

print(f(20,30))

print('\n*** Using the partial function ***')
f = partial(func, 10)

f(20,30)

print('\n*** Using a proxy function ***')
def my_func(a,b, *args, k1, k2, **kwargs):
    print(a,b,args, k1, k2, kwargs)

my_func(10,20,100,200,k1='a', k2='b', k3=100, k4=1000)
def f(x, *args, kw, **kwargs):
    return my_func(10,x, *args, k1='a', k2=kw, **kwargs)

f(20,100,100,200,kw=7, i=78, y=44)


print('\n*** Using a partial function ***')
f = partial(my_func, 10, k1=77)

f(20, 100, 78, k2="v", k3=100, k5=23)


print('\n*** Using a partial ***')
def pow(base, exp):
    print("\t{} ** {} = {}".format(base, exp, base**exp))
    return base**exp

sq = partial(pow, exp=2)
cu = partial(pow, exp=3)
rt = partial(pow, exp=0.5)

print('\tCalling the partial function')
sq(3)
cu(3)
rt(-1)
print('\tBe careful, these partial parameters can be overwritten')
cu(5, exp=5)


a = 2
sq = partial(pow, exp=a)
sq(5)

print('\tThe reference is baked in, ints are immutable')
print('\tSimilar to how default values work')
a = 3
sq(5)

def my_func(a, b):
    print("\t",a,b)


print('\n*** Partials with mutable objects ***')
a = [1,2]
f = partial(my_func, a)

f(100)
# Change a without changing its id
a.clear()
a.append(100)
a.append(200)
# Here the values in the reference the partial points to have changed
# Therefore the partial will produce a different result now
f(100)


print('\n*** Applying partials - sort by euclidean distance ***')
print('\tSort by euclidean distance')

origin = (0, 0)
l = [(1,2), (0,2), (-1,3), (-2,-1), (1,2), (-1,-2), (0, 0)]

euclid_sq = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2
print('\tMake the distance calc a function of one argument only')
partial_sq = partial(euclid_sq, origin)

# Sort by distance
print('\n\tFor sorting the key function must be a function of 1 arg, using a partial')
sorted_l = sorted(l, key=partial_sq)
print("\t", sorted_l)

print('\tUsing a lambda in a similar way directly')
sorted_l = sorted(l, key=lambda x: euclid_sq(origin, x))
print("\t", sorted_l)

print('\tUsing a partial in a similar way directly')
sorted_l = sorted(l, key=partial(euclid_sq, origin))
print("\t", sorted_l)



















