from collections import namedtuple

# When we create a named tuple we get some

Point2D = namedtuple("Point2D", 'x y')

# Two methods for defining defaults, using a prototype and using the defaults property
# prototype, need a default for every field
# defaults property, inject the defaults into the __new__ method

# The defaults __defaults__ property is writable
# We set the default values in the class constructor
# sets default values for the __new__
# We RIGHT align the defaults

# The __defaults__ method is preferred to prototypes
# Docstrings
# Use the namedtuple class factory
Point2D = namedtuple("Point2D", 'x y')
print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)
print(help(Point2D))


# Modify the docs
Point2D.__doc__ = "2D Cartesian Coordinate"
Point2D.x.__doc__ = "x Coordinate"
Point2D.y.__doc__ = "y Coordinate"
print(help(Point2D))
#


#
# *** Using prototypes ***
Vector2D = namedtuple("Vector2D", 'x1 y1 x2 y2 origin_x origin_y')
print(Vector2D._fields)
v1 = Vector2D(0, 0, 10, 10, 0, 0)
# Vector_zero is a vector2d instance
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
# We use vector_zero as a prototype to create new vectors
v2 = vector_zero._replace(x1=10, y1=10, x2=10, y2=20)
# The downside of this approach is kwargs are needed
#     and defaults are needed for every field
#     not transparent or clean, use of replace
# Advantage
#     multiple prototypes possible
#


#
# *** Example using defaults ***
def func(a, b=10, c=20):
    print(a, b, c)


print(func.__defaults__)
# Modifying the defaults right aligned
func.__defaults__ = (100, 200, 300)

func()
# The __init__ is an initializer, it happens after the object has been constructed
# The __new__ happens first, and creates the object
# We want to modify the __new__ method defaults
# Currently there are no defaults
print(Vector2D.__new__.__defaults__)
# Assign new defaults, right align
Vector2D.__new__.__defaults__ = (0, 0)
# The origin_x origin_y now have defaults
v1 = Vector2D(10, 10, 20, 20)
Vector2D.__new__.__defaults__ = (0, 0, 0, 0, 0, 0)
# Now all the fields have default values
v1 = Vector2D()

