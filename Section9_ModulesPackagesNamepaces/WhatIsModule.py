

# Module is an
from pprint import pprint as Print
from types import ModuleType


def func():
    a = 10
    b = 203
    print("\nlocals() to func:" )
    Print(locals())
    return a


#
# # >>> globals()
# # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/jpmolden/Desktop/Python3DeepDiveUdemy/Section9_ModulesPackagesNamepaces/WhatIsModule.py', 'func': <function func at 0x7fb85cdeb8c8>}
# # >>> import pprint
# # >>> pprint.pprint(globals())
# # {'__annotations__': {},
# #  '__builtins__': <module 'builtins' (built-in)>,
# #  '__doc__': None,
# #  '__file__': '/home/jpmolden/Desktop/Python3DeepDiveUdemy/Section9_ModulesPackagesNamepaces/WhatIsModule.py',
# #  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
# #  '__name__': '__main__',
# #  '__package__': None,
# #  '__spec__': None,
# #  'func': <function func at 0x7fb85cdeb8c8>,
# #  'pprint': <module 'pprint' from '/usr/lib/python3.6/pprint.py'>}
# # >>>
#
# # globals() is a dict
#
# f = globals()['func']
#
# print(f())
#
# print(f is func)
#
#
# # Unsuprisingly in the global scope ie main the globals and locals are the same
# print("\nlocals():" )
# Print(locals())

import math
import fractions
print(math.__repr__())
print(func.__repr__())
print(fractions.__repr__())

# Builtins written in C

# Point to same object
junk = math

print(junk.sqrt(2))
Print(globals())

# 1.4142135623730951
# {'Print': <function pprint at 0x7f2c96a6a8c8>,
#  '__annotations__': {},
#  '__builtins__': <module 'builtins' (built-in)>,
#  '__cached__': None,
#  '__doc__': None,
#  '__file__': '/home/jpmolden/Desktop/Python3DeepDiveUdemy/Section9_ModulesPackagesNamepaces/WhatIsModule.py',
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f2c981402e8>,
#  '__name__': '__main__',
#  '__package__': None,
#  '__spec__': None,
#  'fractions': <module 'fractions' from '/usr/lib/python3.6/fractions.py'>,
#  'func': <function func at 0x7f2c98166ea0>,
#  'junk': <module 'math' (built-in)>,
#  'math': <module 'math' (built-in)>}
#

print("\nThe Math entry in the globals dict")
Print(globals()['math'])

New_math_handle = globals()['math']
print("\nNew Math handle \"New_math_handle.sqrt(2)\" = ", New_math_handle.sqrt(2))

# Type is module.. an object
print(type(New_math_handle))
print(id(New_math_handle))
print(id(math))

# When a module is imported it is instantiated in memory, the global dics and the system cache


# System Cache
import sys
# Print(sys.modules)
# Dict: contains our module and its location in memory, reference
print(id(sys.modules['math']))
# Not found as it's already loaded as math
#   Errors Since: print(id(sys.modules['New_math_handle']))


# Math module dict, all the attributes in the math module(object)
print("\n\nMath Module Dict:")
Print(math.__dict__)

function_alias = math.__dict__['sqrt']
print("accessing functions via the dict sqrt(2) = ", function_alias(2))



# Import another module
import fractions
print("\nThe fractions code exists in the sys modules at:..")
Print(sys.modules['fractions'])
print("\nThe fractions dict:..")
Print(fractions.__dict__)

#  '__cached__': '/usr/lib/python3.6/__pycache__/fractions.cpython-36.pyc',
#  '__doc__': 'Fraction, infinite-precision, real numbers.',
#  '__file__': '/usr/lib/python3.6/fractions.py',
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f066206e7b8>,
#  '__name__': 'fractions',
#  '__package__': '',
#  '__spec__': ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f066206e7b8>, origin='/usr/lib/python3.6/fractions.py'),
#  '_gcd': <function _gcd at 0x7f066206b840>,
#  'gcd': <function gcd at 0x7f066206b7b8>,
#  'math': <module 'math' (built-in)>,
#  'numbers': <module 'numbers' from '/usr/lib/python3.6/numbers.py'>,
#  'operator': <module 'operator' from '/usr/lib/python3.6/operator.py'>,
#  're': <module 're' from '/usr/lib/python3.6/re.py'>,
#  'sys': <module 'sys' (built-in)>}



import types
print("\nfractions is a ModuleType: ", isinstance(fractions, types.ModuleType))
print("math is a ModuleType: ", isinstance(math, types.ModuleType))




# Creating our own module type
mod = types.ModuleType('TestModule', 'This is a test module')
# Give functionality
mod.pi = 3.141
mod.hello = lambda: '\nHello!! from mod'
Print(mod.__dict__)
print(mod.hello())

# hello function should be listed in the globals()
hello = mod.hello
Print('hello' in globals())
Print('mod' in globals())
print("\n\n***Globals: ***")
Print(globals())

from collections import namedtuple
mod.Point = namedtuple('Point', 'x y')
p1 = mod.Point(0, 1)
p2 = mod.Point(1, 1)
print("p1 : ", p1)
print("p2 : ", p2)
# Point will now be in the dict of mod
print("\n\n***After additions to mod: ***")
Print(mod.__dict__)

# Getting attributes and dot notation
PT = getattr(mod, 'Point')
print(PT(20,10))
# is the same as...
PT = mod.Point(10, 10)
print(PT)
# is the same as...
PT = mod.__dict__['Point']
print(PT(20, 20))
