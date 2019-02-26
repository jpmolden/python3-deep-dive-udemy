# modules can be imported in a number of ways
# import
# importlib



# when a module is imported:
#     1. Checks the sys.modules to see if the module is cached
#     2. module located - using finders
#     3. module is loaded - (retuned by finder-> ModuleSpec) loaders
#     4. an empty module typed reference is added to the system cache
#     5. module is compiled (optionally) - some already compiled
#     6. module is executed (sets up namespace __dict__)
#         6.1. module.__dict__ is module.globals()



# module finders
#       finders + loaders = importers
#     found in sys.meta_path
#     frozen module is a self contained application
#     PathFinder - to find std library and our own modules (file based module)

#     PathFinder:
#         searches sys.path and package __path__


# importing a package
# eg
# from collections import namedtuple
#
# namedtuple is found in the collections.__path__



# Module properties
# builtin
# import math
# type(math) -> module
# math.__spec__ -> what loader to use and the file
# math.__package__ -> is a package if this has some value
# __file__ (builtin only!!) is NOT a attr of math



# Standard library:
# import fractions
# type(fractions) -> module
# math.__spec__ -> what loader to use and the file
# math.__package__ -> "", if a package if this has some value



# Python modules can be
#     buildins
#     files
#     pre-compiled, frozen, or even inside zi[s
#     anything that can be accessed by a finder and a loader



# For file based modules (PathFinder) then:
#     must be in a path specified by sys.path
#     OR, in a path specified by <package>.__path__

# See PEP302
