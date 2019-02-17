
# Position has meaning
# Use unpacking
# x, y = pt

pt = (10, 20)
import math
dist = math.sqrt(pt[0] ** 2 + pt[1] ** 2)
# Including format specifier and f string
print(f'The distance from the origin is {dist: .2f}')


# We may make this easier using a class nut it's overkill
# Using names tuples gives the easy readability of a class without the overhead
# Downside of classes, they are mutable
# Though they are robust


print('\n*** Named tuples are a subclass of tuple ***')
# Adds property names
from collections import namedtuple

# !!! namedtuple is a class factory, it generates new types
# The new class generated inherits from tuple
# It provides named properties to in access elements of the tuple
# It requires a class name and field names, order of field names matters
# The field names can be any valid names except an _
# The return value from namedtuple will be a class
# We assign the returned class a name

Point2D = namedtuple("Point2D", ['x', 'y'])
Pt2D = namedtuple("Point2D", ['x', 'y'])
# We then create instances of this class
pt1 = Point2D(10, 20)
pt2 = Pt2D(10, 30)
print(type(pt1))
print(type(pt2))


class MyClass:
    pass

# Python creates an object of type MyClass and assigns a label (MyClass) to that object
MyClassAlias = MyClass
# Both are instances of the MyClass class
inst1 = MyClass()
inst2 = MyClassAlias()

# namedtuple creates the class
Pt2DAlias = namedtuple("P2DClassName", ['x', 'y'])
# namedtuple creates the P2DClassName class and returns it to assign out local label Pt2DAlias
# P2DClass name is the name of the class

# Any sequence types for the field names
namedtuple("Point2D", ['x', 'y'])
namedtuple("Point2D", ('x', 'y'))
namedtuple("Point2D", 'x, y')
namedtuple("Point2D", 'x y')
# __new__ uses the field names and comes before the initialization stage

# we can even use keyword args
pt3 = Point2D(x=10, y=40)


# Accessing data in a named tuple
# by index, slicing, iterate
pt4 = Point2D(10, 20)
x, y = pt4
x = pt4[0]


# We can access the data using the field names
x1 = pt1.x


# The Point2D class inherits from tuple, therefore it is immutable!
pt5 = Point2D(10, 30)
# pt5.x = 100  - Cannot change this since an int is immutable and the container pt5 is also immutable


# The rename keyword-only argument for namedtuple (default false) will automatically rename invalid field names
# Person = namedtuple("Person", 'name age _ssn')    - Wont Work, _ not allowed for namedtuple
# This will work and the field name _ssn will become ssn
Person = namedtuple("Person", 'name age _ssn', rename=True)


# Introspection
Person = namedtuple("Person", "name age _ssn", rename=True)
# The field names are stored in the class, we don't need an instance to introspect
print(f"Person.fields = \n\t{Person._fields}")


# namedtuple is a class factory
Point2D = namedtuple("Point2D", 'x y')
p1 = Point2D(10, 20)
# print(p1._source)
# print(f"The named tuple code\n{'*' * 10}\n{Point2D._source}\n{'*' * 10}")


# Extract data as a dictionary
dict_names = p1._asdict()
print(dict_names)













