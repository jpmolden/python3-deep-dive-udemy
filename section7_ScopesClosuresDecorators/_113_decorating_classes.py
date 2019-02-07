# print('\tIf it is then a class can now function like a decorator factory')
# print('\tDecorating my_func with a MyClass instance, which is callable')
#
#
#
#
# print('\n*** The Long Way Round, Equivalent to the @ syntax***')

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

print('\n***Decorator for the Fraction class ***')
def dec_speak(cls):
    cls.speak = lambda self, message: "{0} instance ays: {1}".format(self.__class__.__name__,
                                                                       message)
    # Not needed but follows consistent decorator format
    return cls

# Decorating the Fraction class
Fraction = dec_speak(Fraction)
print(f1.speak("Hi"))









