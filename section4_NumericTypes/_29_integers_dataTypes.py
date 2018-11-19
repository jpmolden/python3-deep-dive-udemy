
# Numeric Types
#     bool
#     int
#     factions.Fraction
#     float
#     decimal.Decimal (to control precision)
#     complex
#

# int (Integers)
#
#     magnitude
#    8-Bits
#         [-128, 127] - Zero does not need a sign, therefor squeeze in an extra number

#    16-Bits - Signed - 2^(16-1) = 32,768
#         [-32,768, 32,767] - Zero does not need a sign, therefor squeeze in an extra number

# 32-Bit OS, 2^32 addresses

# Some languages (Java, C) provide multiple distinct data types that use a fixed number of bits
# Python does not, seamless


print(type(100))
# Import sys module
import sys

print("0", sys.getsizeof(0), "Bytes")
print("1", sys.getsizeof(1), "Bytes")
print("2**1000", sys.getsizeof(2**1000), "Bytes")
# Python handles the amount of memory for an int, unlike c

import time
def calc(a):
    for i in range(1000000):
        a * 2


for a in (10, 100, 1000, 2**10000):
    start = time.perf_counter()
    calc(a)
    end = time.perf_counter()
    print("a = {0} took\t".format(a), end - start, "secs")


# Can use abitrarily large ints in python with only additional computation overhead


