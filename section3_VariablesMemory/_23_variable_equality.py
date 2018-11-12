
# Variable Equality

# Memory Address or Data Equality

# Identity (memory)
# var_1 is var_2
# var_1 is not var_2
# Less clear: not(var_1 is var_2)


# Object State (Data)
# Equality operator
# var_1 == var_2
# var_1 != var_2


#

a = 10
b = a

print("Identity (Memory) - a is b:", a is b)
print("State    (Data)   - a == b:", a == b)


a = "Hello"
b = "Hello"
print("\n*** Assign a and b the same value str literal\n"
      "Python creates a SHARED REFERENCE, ie same mem location ***")
# Python will create a shared reference to this immutable object to save memory
print("Identity (Memory) - a is b:", a is b)
print("State    (Data)   - a == b:", a == b)


a = [1, 2, 3]
b = [1, 2, 3]
print("\n*** Assign a and b the same value list literal\n"
      "Python creates a separate reference, ie diff mem location ***")
print("Identity (Memory) - a is b:", a is b)
print("State    (Data)   - a == b:", a == b)


a = 10
b = 10.0
print("\n*** Assign a and b the same value number, one int, one float\n"
      "Python creates a separate reference, ie diff mem location ***")
print("Identity (Memory) - a is b:", a is b)
print("State    (Data)   - a == b:", a == b)


# The None Object
# assigned to variables to indicate they are not set
# Like a null ptr
# None is an object too, always shared.

a = None
b = None
c = None

# None will always be the same addr in an application
print("\n*** None is an object to indicate no value\n"
      " ***")
print("a is None:", a is None)

a = 10
b = 10
print("hex(id(a)):", hex(id(a)))
print("hex(id(b)):", hex(id(b)))
print("Identity (Memory) - a is b:", a is b)
print("State    (Data)   - a == b:", a == b)

a = 500
b = 500
print("hex(id(a)):", hex(id(a)))
print("hex(id(b)):", hex(id(b)))
print("Identity (Memory) - a is b:", a is b)
print("State    (Data)   - a == b:", a == b)


# No Imaginary component
a = 10 + 0j
b = 10.0
print("a is ", type(a), "b is:", type(b))
print("Identity (Memory) - a is b:", a is b)
print("State    (Data)   - a == b:", a == b)


a = None
b = None
c = None

