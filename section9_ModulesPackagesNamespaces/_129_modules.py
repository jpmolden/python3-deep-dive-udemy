# What is a module
def func():
    a = 10
    return a

print(func)
# Fun is found in the namespace
print(globals())
print(locals())
# In the global scope is the local and global scope the same
print(f'\tIs the local == gloabl : {locals() == globals()}')
print(globals()['func'])

f = globals()['func']
print(f is func)
print(f())


#
a = 100
print(f"The globals contains, a = {globals()['a']}")
def func():
    a = 10
    b = 10
    print(f'The function func has locals : {locals()}')

func()
#


#
#
# What is a module?
print(f"\n\n{'*' * 10} What is a module {'*' * 10}")
import math
# There is a difference between the builtin and the std library functions
# The builtins are written in c
print(math)
import fractions
print(fractions)

junk = math
# The junk label points to the same object
print(junk.sqrt(2))
print(globals()['math'])
mod_math = globals()['math']
print(mod_math.sqrt(2))
# Using maths looks in the globals dict
# When we import it gets loaded into the globals dict
print(type(mod_math))
print(type(math))
print(type(fractions))
# If we import again it does not reload the module
import math
# The reference is added to the globals dict and the system cache
import sys
print(sys.modules)
# This dict contains the module symbol and where it's loaded in memory
print(type(sys.modules))
print(sys.modules['math'])
# Importing math again from another module it will look inside sys modules and find it
#


# Introspection
print(f"\n\n{'*' * 10} Introspection of a module {'*' * 10}")
import math
# Print all the attributes in the math module
print(math.__dict__)
f = math.__dict__['sqrt']
print(f(20))
print(f'\tThe __package__')
print(f'\tThe ModuleSpac: Metadata about the object')
#


#
print(f"\n\n{'*' * 10} Introspection of a module written in C {'*' * 10}")
import fractions
# The fraction.py code has a location
print(sys.modules['fractions'])
print(dir(fractions))
from pprint import pprint
print("\n")
pprint(fractions.__dict__)
# __file__ where the file is located
print(fractions.__dict__['__file__'])
# Modules are loaded from a file, are a module type, have a namespace and are a container of global variables
# Modules have an execution environment (can run code inside)
# There does the module type live
import types
print(f"\tIs fractions a module type: {isinstance(fractions, types.ModuleType)}")
# We can create our own module type
mod = types.ModuleType("test", "This is a test module")
print(f"\tis mod an instance of the module types: {isinstance(mod, types.ModuleType)}")
pprint(mod.__dict__)
# How do we add functionality
mod.pi = 3.14
mod.hello = lambda: "Hello!"
print(mod.__dict__)
print(mod.hello())
# Mod is not in the globals
print('mod' in globals())
#
hello = mod.hello
print('hello' in globals())
hello()


print(f"\n\n{'*' * 10} Introspection of a module written in C {'*' * 10}")
from collections import namedtuple
mod.Point = namedtuple("Point", 'x y')
p1 = mod.Point(1,1)
print(dir(mod))
# A module is just another type of object
# Another way
PT = getattr(mod, "Point")
print(PT(10, 20))
# The same as
PT = mod.__dict__['Point']
print(PT(10, 20))
# The namespaces are those dictionaries
