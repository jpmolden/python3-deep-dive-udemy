from collections import namedtuple

# namedtuples are immutable
Point2D = namedtuple("Point2D", "x y")
pt = Point2D(0, 0)

Stock = namedtuple("Stock", "symbol year month day open high low close")
djia = Stock('DJIA', 2018, 10, 12, 8000, 9000, 7000, 7500)

# If we want a new value for close we'd need to..
# Not very clean
djia = Stock(djia.symbol,
             djia.year,
             djia.month,
             djia.day,
             djia.open,
             djia.high,
             djia.low,
             7600)


# Try wtih slicing
# Unpack all the djia elements except the last one to current
# Unpack to a list
*current, _ = djia
# Unpack current into the new named tuple
djia = Stock(*current, 7500)


# We can use the _make class method but we need to create an iterable first
# Slice to a tuple
current = djia[:7]
new_values = current + (7600,)
djia = Stock._make(new_values)


# What if we only want to change a value in the middle
# Makes no sense with unpacking *pre, day, *post = djia
pre = djia[:3]
post = djia[4:]

new_values = pre + (26,) + post
djia = Stock._make(new_values)


# Still has drawbacks!!
# Modifying 2 values
# Need to slice multiple times


# *** Solution the _replace method ***
# The keyword name must match an existing field name
djia = djia._replace(day=20, close=7001)
print(djia)


# Extending a named tuple
# Stock = namedtuple("Stock", "symbol year month day open high low close")
Point2D = namedtuple("Point2D", 'x y')
Point3D = namedtuple("Point3D", 'x y z')

print(Point2D._fields)
new_fields = Point2D._fields + ('previous_close', )
# Extend using the existing fields to create a new one
StockExt = namedtuple("StockExt", new_fields)

# Extending the values
Stock = namedtuple("Stock", "symbol year month day open high low close")
StockExt = namedtuple("StockExt", Stock._fields + ('previous_close', ))
djia = Stock("DJIA", 2018,1,25,26313,26458,26260,26393)
djia_ext = StockExt(*djia, 26000)
# Or
djia_ext = StockExt._make(djia + (25000,))
print(djia_ext)
















