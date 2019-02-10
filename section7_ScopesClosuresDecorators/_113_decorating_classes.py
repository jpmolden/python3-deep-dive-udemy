# print('\tIf it is then a class can now function like a decorator factory')
# print('\tDecorating my_func with a MyClass instance, which is callable')

# print('\n*** The Long Way Round, Equivalent to the @ syntax***')
from builtins import object, complex
from fractions import Fraction
f = Fraction(2,3)
print(f.denominator)


print('\n*** Monkey patching new attributes ***')
# Monkey patching new attributes
Fraction.speak = lambda self, message: print(message)
f.speak("This is a late parrot, monkey patching new functions onto an existing class")


print('\n*** Monkey patching fraction with in an integral ***')
Fraction.is_integral = lambda self: self.denominator == 1
f1 = Fraction(2, 3)
f2 = Fraction(16, 2)
print(f1.is_integral(), f2.is_integral())

print('\n*** Decorator for the Fraction class ***')


def dec_speak(cls):
    cls.speak = lambda self, message: "{0} instance says: {1}".format(self.__class__.__name__,
                                                                       message)
    # Not needed but follows consistent decorator format
    return cls


# Decorating the Fraction class
Fraction = dec_speak(Fraction)
print(f1.speak("Hi"))


class Person:
    pass

Person = dec_speak(Person)
p = Person()
print(p.speak("Hello"))


from datetime import datetime, timezone

# This is an instance method e.g info self
def info(self):
    # Not a closure
    results = []
    results.append("time: {0}".format(datetime.now(timezone.utc)))
    results.append("Class: {0}".format(self.__class__.__name__))
    results.append("id: {0}".format(hex(id(self))))
    for k, v in vars(self).items():
        results.append("{0}: {1}".format(k, v))
    return results


def debug_info(cls):
    # Decorator
    cls.debug = info
    # For decorator consistency only, cls is mutated
    return cls

# using decorator syntax ie not the Person = debug_info(Person) syntax
@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @staticmethod
    def say_hi():
        return "hello there"


p = Person("Mike", 1986)
print('\n\n*** Decorator for the Person class ***')
print(p.debug())

@debug_info
class Automobile:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        # Psudo-private variables
        self.speed = 0

    # Decorates the self._speed property
    # Same as self.speed = property(self.speed)
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError("Speed cannot exceed the top_speed")
        else:
            self._speed = new_speed


auto = Automobile("Dodge", "Stratus", 12)
print(auto.debug())
try:
    auto.speed = 34
except:
    pass

# Will not have changed speed
print(auto.debug())


from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(-3.1, 2.1)
print(p1)
print(p2)
print(p3)
print(p1 is p2)
print(p2 is p3)
# == defaults to the memory address unless the __eq__ method is set
print(p1 == p2)
print(p1 < p3)
print(p1 < p2)
# print(p1 >= p2)
print('\n\tWith only eq and lt it is possible to construct or infer the others (>, >=, <=')


print('\n\n*** Using class decorators for ordering operations***')
print('\t* a <= b iff a < b or a == b')
print('\t* a >  b iff not(a<b) and a != b')
print('\t* a >= b iff not(a<b)')

print("\t*This is a simple illustration it's not good code")
def complete_ordering(cls):
    if "__eq__" in dir(cls) and "__lt__" in dir(cls):
        # Generally speaking do not monket patch __ methods like this
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not(self < other)
    # Not needed since we are mutating the class unless we want to use the @decorator syntax
    return cls


print('\n\n*** Using the complete ordering decorator ***')


@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(-3.1, 2.1)
print(p1)
print(p2)
print(p3)
print(p1 is p2)
print(p2 is p3)
# == defaults to the memory address unless the __eq__ method is set
print(p1 == p2)
print(p1 < p3)
print(p1 < p2)
# Implemented by the decorator for the class
print(p1 >= p2)
print(p1 != p2)


print('\n\n*** Python has a standard library for this!!  ***')

from functools import total_ordering
print('\tUsing total_ordering decorator')
print('\tThis decorator figures out all the missing comparison operators'
      ' and completes the set')


@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Point):
            return abs(self) > abs(other)
        else:
            return NotImplemented


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(-3.1, 2.1)
print(p1)
print(p2)
print(p3)
print(p1 is p2)
print(p2 is p3)
print(p1 == p2)
print(p1 < p3)
print(p1 < p2)
print(p1 >= p2)
print(p1 != p2)


print('\tThe total_ordering class decorator can be used to complete the comparison operators '
      'without specifying each')








