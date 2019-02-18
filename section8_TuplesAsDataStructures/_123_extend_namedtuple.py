from collections import namedtuple

Point2D = namedtuple("Point2D", 'x y')
pt = Point2D(10, 20)

# Named tuples are immutable
# Create a new point
print(hex(id(pt)))
pt = Point2D(100, pt.y)
# A new memory address
print(hex(id(pt)))


# Using unpacking
Stock = namedtuple("Stock", "symbol year month day open high low close")
djia = Stock("DJIA", 2018,1,25,26313,26458,26260,26393)
*values, _ = djia


values.append(27000)
# Unpack into a new stock
djia = Stock(*values)
print(djia)


# Using slicing
values = djia[:7]
djia = Stock(*values, 1000)
print(djia)


# Using the replace method
djia = djia._replace(year=2017, open=10000)
print(djia)


# Using the make method takes an iterable
values = djia[:7]
# Accepts an iterable
djia = Stock._make(values + (100,))


# Extending a namedtuple
# Simple way
# Point3D = namedtuple("Point3D", 'x y z')
# Add extra field
Point2D = namedtuple("Point2D", 'x y')
Point3D = namedtuple("Point3D", Point2D._fields + ('z', ))


# Using the values
pt = Point2D(10, 20)
# Unpack the point into a new 3d point
pt3d = Point3D(*pt, 100)
print(pt3d)











