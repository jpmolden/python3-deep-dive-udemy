import sys
from pprint import pprint

# print("\tImporting _module1")
# import _138_module1
#
# # When a package module is imported it's code is executed like a regular codefile
# print("\tImporting pack138")
# import pack138
#
# # The finder needs to know more on how to find sub packages
# print("\tImporting pack138.pack138_1")
# import pack138.pack138_1
#
#
# #
# print("\n**** _module1 ****")
# # Module have a file property
# print(f"module1's file property: {_138_module1.__file__}")
# # Not in any package because it is in the root of the application
# print(f"module1's package property: {_138_module1.__package__}")
# # Path is only for packages, so this is n
# print(f"module1's path property: {getattr(_138_module1, '__path__', None)}")
#
#
# #
# print("\n**** pack1 ****")
# #
# # The code file for packages in in the __init__ file
# print(f"pack1's file property: {pack138.__file__}")
# # the pack1 packages
# print(f"pack1's package property: {pack138.__package__}")
# # only packages have a path property
# print(f"pack1's path property: {getattr(pack138, '__path__', None)}")
# # Python stitches the __init__ and package dir together
# # We have access to value from the package __init__ file since it executed and is now
# # in the globals
# print(f"pack1 value: \"{pack138.value}\"")
#
#
# #
# print("\n**** packages are modules that contain other modules (inc other packages) ****")
# # Packages are modules
# print(f"Type pack1: {type(pack138)}")
# print(f"Type _module1: {type(_138_module1)}")
#
#
# print("\n**** sub packages ****")
# # Pack pack1_1 is not in either the globals or sys.modules
# print(f"'pack138_1' in globals(): {'pack138_1' in globals()}")
# print(f"'pack138_1' in sys.modules: {'pack138_1' in sys.modules}")
# print(f"pack138.pack138_1.value: \'{pack138.pack138_1.value}\'")
# print("Imports of sub modules (pack138.pack138_1) means that only the top level package is in globals ")
# print(f"'pack138.pack138_1' in globals(): {'pack138.pack138_1' in globals()}")
# print(f"'pack138.pack138_1' in sys.modules: {'pack138.pack138_1' in sys.modules}")
#
#
# #
# print("\n**** importing sub packages directly ****")
# from pack138 import pack138_1
# # The same value since all this does is give a direct hangle to the globals namespace
# print(f"id(pack138_1) == id(sys.modules['pack138.pack138_1']): {id(pack138_1) == id(sys.modules['pack138.pack138_1'])}")


#
print("\n**** importing sub modules ****")
import pack138.pack138_1.module1b
print(f"{'pack138' in sys.modules}")
print(f"{'pack138.pack138_1' in sys.modules}")
print(f"{'pack138.pack138_1.module1b' in sys.modules}")
# The only symbol that gets added to the namespace is pack1
pprint(globals())
# python does not put in the others to avoid the chance of name collision



