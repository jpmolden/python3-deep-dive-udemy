
# Sometimes classes are not needed
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z}"

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented


# Named tuples are immutable
from collections import namedtuple
Point2D = namedtuple("Point2D", ['x', 'y'])
# Same as
Pt3D = Point3D

# Create an instance
p1 = Point2D(x=10, y=20)

print(f"Is this an instance of a tuple = {isinstance(p1, tuple)}")
# To create and instance of Point3D

# We get alot of tuple stuff for free also
a = (10, 20)
b = (10, 20)

print(f"a is b: {a is b}")
print(f"a == b: {a == b}")

# We would not get the == or the repr for free with a class
p1 = Point2D(10, 20)
p2 = Point3D(10, 20, 30)

print(f"Finding the max is easy max: {max(p1)}")
# print(f"Not so for a class it's not iterable!!: {max(p2)}")


# Other free stuff
# Vectors in 2 and 3 d space
# Find the dot product
# a = a.x, a.y
# b = b.x, b.y
# a.b = a.x * b.x + a.y * b.y
def dot_procuct_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

pt1 = Point3D(1, 2, 3)
pt2 = Point3D(1, 1, 1)
print(dot_procuct_3d(pt1, pt2))


print(list(zip(a, b)))
# Using list comprehension
sum([e[0] * e[1] for e in zip(a, b)])


def dot_procuct(a, b):
    return sum([e[0] * e[1] for e in zip(a, b)])

p1 = Point2D(10,  20)
p2 = Point2D(12,  21)
print(f"The dot product is :{dot_procuct(p1, p2)}")

# This is more versatile than the original doc_product_3d
Vector3D = namedtuple("Vector3D", "x y z")
p3 = Vector3D(10, 20, 30)
p4 = Vector3D(10, 2, 60)
print(f"The dot product is :{dot_procuct(p3, p4)}")

print(p3)
# Getting back the plain tuple
t3 = tuple(p3)
print(t3)

# We can slice
print(p3[0:2])
# Use names
print(p3.x)


Circle = namedtuple("Circle", "center_x center_y  radius")
c = Circle(0, 0, 10)
print(c.radius)


# Using multiline strings
Stock = namedtuple("Stock", '''symbol
                                year
                                month
                                day
                                open
                                high
                                low
                                close''')

djia = Stock("DJIA", 2018, 12, 30, 26000, 37000, 18000, 25000)
print(djia)

# We can access with property names, iterate
for item in djia:
    print(item)

# we can unpack too
p = Point2D(10, 20)
x, y = p

# Extended unpacking
symbol, month, day, *_, close = djia
print(symbol, month, day, close)


# _ is a valid variable name, convention is don't care
# _ can't be used in nametuple field name
# Person = namedtuple("Person", "name age _ssn")
#
Person = namedtuple("Person", "name age _3 _ssn", rename=True)

# Introspection
print(Person._fields)
# print(djia._source)
print(djia._asdict())
# An ordered dict is a special dictionary preserves the ordering of the keys

# The class holds the extra overhead but each instance is essentially a tuple










