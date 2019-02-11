
print('\n*** Create a better solution than a hardcoded registry ***')
print('\tA better dispatcher')
print('\tA decorator')

def single_dispatch(fn):
    registry = {}
    registry[object] = fn
    registry[int] = lambda a: "{0}(<i>{1}</i>".format(a, str(hex(a)))
    registry[str] = lambda s: escape(s).replace("\n", "<br/>\n")
    # Assume only a single argument

    def inner(arg):
        # Get the registered fn and call, default to obj if not found
        f = registry.get(type(arg), registry[object])
        return f(arg)
    return inner

from html import escape

# This becomes the default function associated with the object registry key
@single_dispatch
def htmlize(a):
    return escape(str(a))

print(htmlize("1 < 100"))
print(htmlize(100))


print('\n*** Create an even better decorator, no hardcoded values ***')
print('\tCreate a parameterized decorator inside a decorator')

def single_dispatch(fn):
    registry = {}
    registry[object] = fn

    def decorated(arg):
        # Get the registered fn and call, default to obj if not found
        f = registry.get(type(arg), registry[object])
        return f(arg)

    def register(type_):
        # This us  a parameterized decorator
        def inner(fn):
            # Registry is a free variable inside the closure
            registry[type_] = fn
            return fn
        return inner

    def dispatch(type_):
        return registry.get(type_, registry[object])

    # Adding attributes to the decorated closure
    decorated.register = register
    decorated.registry = registry
    decorated.dispatch = dispatch
    return decorated


@single_dispatch
def htmlize(a):
    return escape(str(a))

print(htmlize("1 < 100"))

print('\tThis register decorator can be used to changes the registered types on the fly')
@htmlize.register(int)
def html_int(a):
    return "{0}(<i>{1}</i>".format(a, str(hex(a)))

print(htmlize(100))
print(htmlize.registry)

print('\tRegistering the sequence types')
@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = ("<li>{0}</li>".format(htmlize(item))
             for item in l)
    return "<ul>\n" + "\n".join(items) + "\n</ul>"

print(htmlize([1,32,35]))
print(htmlize((1,10,20)))

# Alternative syntax
# html_list = htmlize.register(list)(html_list)
print('\tGetting the registry')
print(htmlize.registry)

print('\tThe problem is we are looking up the type of the argument, we register based on type')
print('\tWe should use something more generic, abstract base classes')

from numbers import Integral

class Person:
    pass

class Student(Person):
    pass

p = Student()
print("Using type is too limited for dispatching, type:", type(p))
print("Using is isinstance is more generic, is p a Person:", isinstance(p, Person))
print("Using is isinstance is more generic, is p a Student:", isinstance(p, Student))


@single_dispatch
def htmlize(a):
    return escape(str(a))

# @htmlize.register(Integral)
def html_integral_number(a):
    return "{0}(<i>{1}</i>".format(a, str(hex(a)))


from collections.abc import Sequence
print(isinstance([1,2,3], Sequence))
print(type([1,2,3]) is Sequence)
print(isinstance((1,2,3), Sequence))
print(type((1,2,3)) is Sequence)

print('\tThe problem is we are looking up the type of the argument, we register based on type not based'
      'on abc, abstract base classes')
