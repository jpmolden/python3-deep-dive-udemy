

from pprint import pprint
import operator
pprint(dir(operator))

x =['__abs__',
 '__add__',
 '__all__',
 '__and__',
 '__builtins__',
 '__cached__',
 '__concat__',
 '__contains__',
 '__delitem__',
 '__doc__',
 '__eq__',
 '__file__',
 '__floordiv__',
 '__ge__',
 '__getitem__',
 '__gt__',
 '__iadd__',
 '__iand__',
 '__iconcat__',
 '__ifloordiv__',
 '__ilshift__',
 '__imatmul__',
 '__imod__',
 '__imul__',
 '__index__',
 '__inv__',
 '__invert__',
 '__ior__',
 '__ipow__',
 '__irshift__',
 '__isub__',
 '__itruediv__',
 '__ixor__',
 '__le__',
 '__loader__',
 '__lshift__',
 '__lt__',
 '__matmul__',
 '__mod__',
 '__mul__',
 '__name__',
 '__ne__',
 '__neg__',
 '__not__',
 '__or__',
 '__package__',
 '__pos__',
 '__pow__',
 '__rshift__',
 '__setitem__',
 '__spec__',
 '__sub__',
 '__truediv__',
 '__xor__',
 '_abs',
 'abs',
 'add',
 'and_',
 'attrgetter',
 'concat',
 'contains',
 'countOf',
 'delitem',
 'eq',
 'floordiv',
 'ge',
 'getitem',
 'gt',
 'iadd',
 'iand',
 'iconcat',
 'ifloordiv',
 'ilshift',
 'imatmul',
 'imod',
 'imul',
 'index',
 'indexOf',
 'inv',
 'invert',
 'ior',
 'ipow',
 'irshift',
 'is_',
 'is_not',
 'isub',
 'itemgetter',
 'itruediv',
 'ixor',
 'le',
 'length_hint',
 'lshift',
 'lt',
 'matmul',
 'methodcaller',
 'mod',
 'mul',
 'ne',
 'neg',
 'not_',
 'or_',
 'pos',
 'pow',
 'rshift',
 'setitem',
 'sub',
 'truediv',
 'truth',
 'xor']

# Same
x = 1+2
operator.add(1,2)

print('\n*** Operators ***')
print("add: ", operator.add(1,2))
print("mul: ", operator.mul(1,2))
print("truediv: ", operator.truediv(1,2))
print("floordiv: ", operator.floordiv(13,2))

from functools import reduce
print("Mult all:", reduce(lambda x,y: x*y, [1,2,3,4]))

print("Mul operator:", reduce(operator.mul, [1,2,3,4,5]))

from operator import is_
print(is_('abc', "def"))




print('\n*** Attribute getters and setters ***')
l = [1,2,3,4]
g = operator.getitem(l, 1)
print(g)

l[1] = 10
del l[3]
print(l)
l = [1,2,3,4]
g = operator.setitem(l, 1, 10)
g = operator.delitem(l,3)
print(l)

print('\n*** Item getter, think like a partial function ***')
f = operator.itemgetter(2)
print("\tf is a callable: ", type(f))
print("\tGet item(from list)  ", f(l))
s = "Python"
print("\tGet item(from string)", f(s))
f = operator.itemgetter(-1, -2, 0)
print("\tGet item(from string)", f(s))
l = [1,2,3,4,5]
print("\tGet items(from list)  ", f(l))




print('\n*** Attribute getter ***')
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self, c):
        print("\t", self.a, self.b, c)
        print("\tTest method running...")


obj = MyClass()
print("\t** obj **:", obj)
print("\t", obj.a)
print("\t", obj.b)
print("\t", obj.c)
print("\t", obj.test)
# print("\t", obj.test())

prop_a = operator.attrgetter("a")
print("\tobj attribute", prop_a(obj))

my_var = "b"
prop_b = operator.attrgetter(my_var)
print("\t", prop_b(obj))

my_var = "c"
prop_b = operator.attrgetter(my_var)
print("\t** Still the same value - Immutable!! **", prop_b(obj))

print("\tGetting multiple attributes", operator.attrgetter("a", "b")(obj))
tup = operator.attrgetter("a","b","test")(obj)
print("\t", tup)


print('\n*** Using Lamdas to do the same ***')
f = lambda x: (x[2], x[3])
x = [1,2,3,4,5]
print("\tGetter using lambda", f(x))



print('\n*** Sorting complex numbers ***')
l = [5+2j, 1+2j, -1-2j, 7+3j, 0+1j, -3-5j, 1+1j]
# Attribute getter returns a callable which expects a single arg, same as key wants
print("\tSorted based on real", sorted(l, key=operator.attrgetter("real")))

l = [(2,3,4), (1,3,5), (6,), (4,100)]
print("\tSort according to the first element", sorted(l, key=operator.itemgetter(0)))


obj = MyClass()
f = operator.attrgetter('test')
# f(obj)()

print('\tA better way to call single methods, the method caller')
f = operator.methodcaller("test", 1000)
print("\tCall the method")
f(obj)
print('\tWhat about extra parameters')


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self, c, d, *, e):
        print("\t", self.a, self.b, c,d, e)
        print("\tTest method running...")


obj = MyClass()
f = operator.methodcaller('test', 55,56,e=10)
f(obj)
# Same thing
f = operator.attrgetter('test')
f(obj)(10,10,e=12)

# Method caller calls right away





