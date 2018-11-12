# If two variables reference the same ofject in memory


# Python variables are memory references
a = 10
# Set ref of be to be the mem reference of a
# Same obj in memory
b = a


def my_func(v):
    return 1

t = 20
# Pass reference of t into function
my_func(t)


a = 10
b = 10

print("Python automatically points a and b to same memory location, as Shared References\n"
        "\ta = {0}  hex(id(a) : {1}\n"
        "\tb = {2}  hex(id(b) : {3}\n".format( a, hex(id(a)), b, hex(id(b)) ))

print("Is this safe: YES!!!! Ints are immutable SO python creates shared memory references")


a = [1, 2, 3]
b = a
b.append(100)

print("a and b are now lists, and mutable!! So after appending to b:\n"
        "\ta = {0}  hex(id(a) : {1}\n"
        "\tb = {2}  hex(id(b) : {3}\n".format( a, hex(id(a)), b, hex(id(b)) ))

print("Why? Because b is pointing to the same memory location as a"
      "Modifying b will modify a")

