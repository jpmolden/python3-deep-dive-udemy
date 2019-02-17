print('\n*** **')
# The ,'s define the tuple
(10, 20, 30)

a = (10, 20, 30)
b = 10, 20, 30


def print_tuple(t):
    for e in t:
        print(e)


# The ( )'s are needed for function calls
print_tuple((10, 20, 30))
a = "a", 10, 200
print(a[0])
print(a[1])
print(a[2])

print('\tSlice the tuple')
a = "a", 10, 200, 55, 500, "f", 2
print(a[0:2])
print(a[:3])
print(a[-2:])
print(a[-2:3])
print(a[-2:10])

print('\tIterate')
for e in a:
    print(e)

print('\tUnpacking')
x, y, z, *_ = a

print('\tExtended unpacking')
a = 1, 2, 3, 4, 5
x, *_, y, z = a
print("x =", x, ", other =", _, ", y =", y, ", z =", z)
a = 1, 2, 3, 4, 5, 6, 7
x, *_, y, z = a
print("x =", x, ", other =", _, ", y =", y, ", z =", z)


print('\tMutability - The tuple is immutable but the contents may not be..')
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Using f-Strings
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

a = Point2D(10,  20)
b = Point2D(0 , -10)

print(str(a))
print(hex(id(a)))
print(str(b))
print(hex(id(b)))

a = Point2D(0,0), Point2D(0,20)
print(id(a[0]))
print(a[0])
a[0].x = 100
print(id(a[0]))
print(a[0])


print('\tMutability - assignment creates a new tuple')
a = (1,2,3)
print(id(a))
a += (2,3)
print(id(a))

print('\n\tTuples may use any convention we like')
london   = ("London",   "UK",  8_780_000)
new_york = ("New York", "UK",  8_500_000)
beijing  = ("Beijing",  "UK", 21_000_000)

cities = [london, new_york, beijing]
print('\n*** List comprehension *** ')
print("Total population:", sum(city[2] for city in cities))


print('\n*** Unpacking *** ')
record = "DJIA",  2018, 1, 19, 25000, 27000, 22000, 23000
symbol, *_, close = record
print(symbol, "closed at:", close, "\t\t", _)


print('\n*** Unpacking *** ')
for city, country, population in cities:
    # This is how enumerate works
    print(city, country, population)

for index, city in enumerate(cities):
    print(index, "  ", city)


print('\n*** Calculate the approx value of pi *** ')
from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)
    
    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    return random_x, random_y, is_in_circle


print('\n*** Approximate the value of pi *** ')
num_attempts = 10000
count_inside = 0
square_area = 2 * 2
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {square_area * count_inside / num_attempts}')

print('\t')
print('\t')
