from math import floor

# Support for operations
#     +
#     -
#     *
#     /  - Will always return a float
#     **
#

# 10 / 2 = 5 (float)

# floor division - //
# returns 38
print(155 // 4)

# modulo - %
# returns 3
print(155 % 4)

n = 155
d = 4

print("{0} / {1} = {2} remainder {3}".format(n, d, (n // d), (n % 4)))
print("\tn = d * (n // d) + (n % d)")
print("\t{numer} = {denom} * ({numer} // {denom}) + ({numer} % {denom})".format(numer=n, denom=d))

print("*** Floor division ***")
print("\tfloor of 3.199 =", floor(3.199))
print("\tfloor of -3.1 =", floor(-3.1))
print("\ta // b = floor(a / b)")
n = 135
b = 4
n = d * (n // d) + (n % d)
print(n)

print("*** negative numbers ***")
n = -135
d = 4
n = d * (n // d) + (n % d)
print("\tnumer = {numer}\n\tdenom = {denom}".format(numer=n, denom=d))
print("\t{numer} // {denom} = {result}".format(numer=n, denom=d, result=(n // d)))
print("\t{numer} % {denom} = {result}".format(numer=n, denom=d, result=(n % d)))
print("\t** // and % must satisfy **")
print("\tn = d * (n // d) + (n % d)")

print("*** Types *** ")
print("\t", type(10 / 2))
print("\tfloor(-3.14)", floor(-3.14))
print("\t", floor((-3.00000000001)))
# Limited precsion - results in 3
print("\t", floor((-3.0000000000000000001)))


print("\t")


