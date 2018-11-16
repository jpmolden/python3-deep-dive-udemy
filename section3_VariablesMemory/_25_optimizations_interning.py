# CPython, the standard version of python

# Other implementations:

# Jython written in Java, import and use any Java class
#     runs JVM

# IronPython - written in C# and targets .Net

# PyPy - Writen in RPython (statically typed python subset written in C
#             designed to write interpreters)

# .... more


# CPython version


# both references to same point in memory (shared reference)
a = 10
b = 10

print("id(a) = {0}, id(b) = {1}, Same id: {2}".format(id(a), id(b), id(a) == id(b)))


# both references to same point in memory (shared reference)
c = int(257)
d = int(257)
print("id(c) = {0}, id(d) = {1}, Same id: {2}".format(id(c), id(c), id(c) == id(c)))

