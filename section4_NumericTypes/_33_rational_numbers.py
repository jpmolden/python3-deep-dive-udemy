

from fractions import Fraction

x = Fraction(3,45)
fl = float(3.1474564567895615489756)

fl_frac = Fraction(fl)

# Fractio(other_frac)
# Fractio(float)
# Fractio(decimal)
# Fractio(string)
# Fractio("22/7")  -> Fraction(22, 7)


# Other operators
#     +,-,*,/ -> Another Fraction

# Floats have finite precision
print('\tany float can be written as a faction')
import math

x = Fraction(math.pi)
print('x = {}'.format(x))


print('*** Problems converting certain rational floats to clean rationals ***')
print('\tOne big problem of note')
print('\tFraction(0.125)')
print("\t", Fraction(0.125))
print('\tFraction(0.3)')
print("\t", Fraction(0.3))

print('\t', format(0.3, '0.25f'))
print('\tWhats actually stored')
print('\t', format(0.3, '0.10f'))

print('\tusing the limit denominator method')
x = Fraction(math.pi)
x = x.limit_denominator(10)
print("\t{}".format(x))

print('\n*** Can use std operators ***')
print('+ - * / - Will always return fraction object')
print("\t{x} = {numer} / {denom}".format(x=x, numer=x.numerator, denom=x.denominator))

a = 0.125
print(a)
b = 0.3
print(format(b, '0.100f'))
print('\tlimit the denom')
x = Fraction(b)
print(x.limit_denominator(10000))


