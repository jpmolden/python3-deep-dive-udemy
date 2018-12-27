
print('\n*** Using Classes to Decorate Functions ***')
print('\tClasses can be used to decorate in the same way as decorator factories')

# A simple decorator factory
def my_dec(a, b):
    def dec(fn):
        # dec is also a closure
        def inner(*args, **kwargs):
            # Inner function is a closure
            print("\tDecorated function called: a={0} b={1}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec


@my_dec(10, 20)
def my_func(s):
    print("\tHello {0}".format(s))


my_func("Worlds")


print('\n*** Class instances are also callable ***')

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        """
        This makes the instance callable
        """
        print("\tcalled a={0}, b={1}, c={2}".format(self.a, self.b, c))


obj = MyClass(10, 20)
obj(12)
obj.a = 12
obj.__call__(10)



print('\n*** What if __call__ was the decorator ***')

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        """
        __call__ is now a decorator, the class is the dec factory
        """
        def inner(*args, **kwargs):
            # Inner function is a closure
            print("\tDecorated function called: a={0} b={1}".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

print('\tIf it is then a class can now function like a decorator factory')
print('\tDecorating my_func with a MyClass instance, which is callable')
@MyClass(10, 20)
def my_func(s):
    print("\tHello {}".format(s))

my_func("Pete")



print('\n*** The Long Way Round, Equivalent to the @ syntax***')
obj = MyClass(10,15)

def my_func(s):
    print("\tHello {}".format(s))

my_func = obj(my_func)

my_func("Worlds")

