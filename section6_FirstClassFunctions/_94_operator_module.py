
from functools import reduce
l = [2,3,4]
product = reduce(lambda x,y: x * y, l)
print("\t", product)


print('\n*** The operator module ***')
print('\tadd(a,b), mul, pow, mod, floordiv, neg....')

print('\n\tcompare and boollean, lt, le, gt, ge, eq, ne, is_, is_not')
print('\tand_, or_, not_')


print('\n\tSequence/Mapping operations')
print('\tconcat, contains, countOf, getitems, setitem, delitem')
print('\tset and get only work on mutable items')


from operator import itemgetter, getitem, attrgetter, methodcaller
print('\n*** Item getter, returns callable ***')
s = [5,6,7,8]

print(getitem(s, 1))
# Get the 2nd, 3rd, 4th items
g = itemgetter(1,2,3)
print('\titemgetter returns a callable')
print(g(s))
# Call immediately
print(itemgetter(0,1,2)(s))


class My_obj():
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def method1(self):
        print("\t", self.a)

    def method2(self):
        print("\t", self.b)


my_obc = My_obj()
my_obc.a = 10
my_obc.b = 20
my_obc.c = 30
print('\tattrgetter returns a callable')
f = attrgetter('a')
print("a = {}".format(f(my_obc)))

f = attrgetter('a', 'b')
# Use unpacking
print("a = {}, b = {}".format(*f(my_obc)))

print("Call method 1 and method 2 in the my_obj")
[i() for i in attrgetter('method1', 'method2')(my_obc)]


print('\n*** Simpler way use the methodcaller function ***')
print('\tRetrieves a named attribute and calls it as well')
methodcaller('method1')(my_obc)





