import sys
# The hard part is knowing where the file is
# import knows how to find imports

print(sys)
import collections
# import the collections package
print(collections)

# There is more to import than just compiling and exec the code and putting into the sys.modules cache
mod_name = 'math'
# import mod_name
#
import importlib
import importlib.util
# Use the import lib package
print(importlib)

# Import the module and put into the sys.modules dict
# We don't have a handle yet in globals()
importlib.import_module(mod_name)
if 'math' in sys.modules:
    print("We have imported math")

# Get a handle
# math2 = sys.modules['math']
# print(math2.sqrt(2))
# Another way to get a handle
math2 = importlib.import_module(mod_name)
if 'math2' in globals():
    print("We have a handle on math as math2")

if id(math2) == id(sys.modules['math']):
    print("It is the same object")

# .py
# .pyc - compiled python files
# .so
# .pyd

# .zip - python can read into zip
# .egg .wheel
#

#
# The python importer is quite complex
#     finders - Finds the module we want to import, searches for modules, what loader to use
#     loaders - load code, compile, exec and put into cache and may puts symbol into the globals
#               returns a ModuleSpec
#     finder + loader = importer

import fractions
# The finder comes back with a module spec
print(f"\n{'==' * 20}")
print(f"{'*' * 20} Finders {'*' * 20}")
print("\t", fractions.__spec__)
# Print the finder objects
print("\t", sys.meta_path)
import math
print("\t", math.__spec__)
# modules might not be a file you can write your own finders and loaders
# Find but don't load the module
print(importlib.util.find_spec("decimal"))
print(f"{'==' * 20}")


print(f"\n{'==' * 20}")
print(f"{'*' * 20} importing a module {'*' * 20}")
# Create a file
with open('module2.py', 'w') as code_file:
    code_file.write("print('running module2.py..')\n")
    code_file.write("a = 100\n")
print("\tCan we find the module and know how to load it\n\t", importlib.util.find_spec("module2"))
import module2
# module2 is ran and is now in our namespace
print(f"module2 a: {module2.a}")
print(f"{'==' * 20}")


# importing a module from some other path
#
print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} Importing a module from some other path {'*' * 20}")
import os
# Windows home dir
ext_module_path = os.environ['HOMEPATH']
file_abs_path = os.path.join(ext_module_path, 'module3.py')
print(f"\tfile abs path = {file_abs_path}")
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('\trunning module3.py..')\n")
    code_file.write("a = 100\n")

# Can importlib find the spec - NO!!
print(f"\tThe import lib spec for module3:\n\t {importlib.util.find_spec('module3')}")
# If we add this path to the sys paths we can... NO RECOMMENDED!!
sys.path.append(ext_module_path)
print(f"\tAfter adding to sys.path we can find the spec for module3:\n\t {importlib.util.find_spec('module3')}")
# Now importlib knows how to find and how to load this module
import module3
# There are problems adding to sys.path!!
# A better way..
print(f"{'==' * 20}")
