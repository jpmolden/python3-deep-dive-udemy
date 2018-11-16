# Data Types
#     int
#     bool
#     float
#     str
#     list
#     tuple
#     set
#     dict
#     NoneType

# Operators (+, -, ==, is. ...)
# Functions
# Classes
# Types

# These are ALL Objects (including Classes themselves, instance of class type)
# They all have memory addr


# def my_func():


# Memory addr of a function
#     my_func   - Name of the function
#     my_func() - Invoke the function


# Can assign a function to a variable
# Functions can be passed to functions

# Any object can be returned from a function
#     including other functions

a = 10
print("type(a): ", type(a))

# Use standard intiantiation notation, int is a class
b = int(10)
print("type(b): ", type(b))


c = int()
c = int('101', base=2)
print("c = ", c)

print("\n**** Functions are objects too ****")
# print("")
def square(a):
    return a ** 2

print("\ttype(square): ", type(square))
f = square
print("\tid(square): ", id(square))
print("\tid(f):      ", id(f))
print("\t", f(2))

def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


print("\n**** Functions can be passes as return objects and invoked ****")
print("       Can Return functions from other functions")
f = select_function(1)
print("\tf is square:", f is square)
print("\tf(2):", f(2))
f = select_function(2)
print("\tf is square:", f is square)
print("\tf(2):", f(2))


print("       Selecting the cube function then cubing")
print("\tselect_function(2)(3):", select_function(2)(3))

def exec_function(fn, n):
    return fn(n)

print("       Invoking a function withthin another function")
# Passing reference to cube
print("\texec_function(cube, 3):", exec_function(cube, 3))





