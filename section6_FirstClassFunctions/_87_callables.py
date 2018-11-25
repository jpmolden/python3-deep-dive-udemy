

print('*** What are they ***')
print('\tCallable with object()')
print('\tAlways return a value')
print('\tCan check with callable module')
callable(print)
callable('abc'.upper)
callable(str.upper)
callable(callable)

print('\n\tNot callable')
callable(10)

print('\n*** Types of callables ***')
print('\tbuiltin functions - print, len, callable')
print('\tbuiltin methods - a_str.upper a_list.append')
print('\tuser defined functions - def, lambda')
print('\tmethods - functions bound to an object')
print('\tclasses - MyClass(x,y,z) -> calls __new__(x,y,z) -> __init__(self, x,y,z)')
print('\tclass instances - __call__')
print('\tothers - generators, coroutines, asynchronous generators')


print('\n*** Callable function ***')
callable(print)
result = print("hello")
print("\tAll callables return a value")
print(result)

l = [1,2,3]
print(callable(l.append))
s = 'abc'
print(callable(s.upper))
result = s.upper()
print(result)

print('\n\tClasses are callable')
from decimal import Decimal
print(callable(Decimal))


class MyClass:
    def __init__(self, x=0):
        print("initializing")
        self.counter = x


print(callable(MyClass))
a = MyClass(100)
a.counter = 10
print('\tInstances may or may not be callable')
print(callable(a))

print('\n\tMaking the instance callable')
class MyClass:
    def __init__(self, x=0):
        print("initializing")
        self.counter = x

    def __call__(self, x=1):
        print("calling __call__")
        self.counter += x


b = MyClass()
# Any instance method can be called like this
MyClass.__call__(b, 10)
print("Now callable Instance:", callable(b))
print(b.counter)
print('\tCalling')
# A better way to call the instance
b(100)
print(b.counter)

# Callable classes and instances are not the same a functions
print(type(int))
print(type(MyClass))
print(type(str))
print(type(b))





