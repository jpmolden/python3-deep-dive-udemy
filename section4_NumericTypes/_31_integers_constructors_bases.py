

# an int is an object, int class instance

print("*** Ints will work with other numeric data types ***")
a = int(10)
print(int("123", 36))

import fractions
a = fractions.Fraction(22,7)
print("a:", int(a))


# Base 2
print("\n*** Other bases ***")
print("\t", int("1010", 2))
print("\t", int("1010", base=2))
print("\t", int("A12F", base=16))
print("\t", int("a12f", base=16))
a = 0b1010101110001
print("\t", a)


# Recognize 0-9 and a-z, total 36
# Can recognize base 36

print("\n*** reversing the process ***")
number = int("0x10", base=16)
print("\t{type} {value} = {rep}".format(type="Binary", value=number, rep=bin(number)))
print("\t{type} {value} = {rep}".format(type="Octal ", value=number, rep=oct(number)))
print("\t{type} {value} = {rep}".format(type="Hex   ", value=number, rep=hex(number)))


print("*** Other bases ***")
print("\tNeed custom code")

# Base 10
number = 100
b = 23
print("\tn = (n // b) * b + (b % b)")
print("\tConvert base - Ultimatly always in binary")


print("\n*** Represent in different bases ***")

def from_base10(n, b):
    if b < 2:
        raise ValueError("Base must be >= 2")
    if n < 0:
        raise ValueError("Number must be >= 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("Digit map not long enough to encode digits")
    encoding = ''
    encoding = ''.join(digit_map[d] for d in digits)
    return encoding


def rebase_from10(number, base):
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base < 2 or base > 36:
        raise ValueError("Invalid base")

    sign = -1 if number < 0 else 1
    number *= sign
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

a = rebase_from10(-5675, 16)
print("a = 0x{}".format(a))
print(int(a, base=16))
