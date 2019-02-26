# Packages are modules
# Modules might not be packages

# ** They are modules that can contain modules **

# packages can contain sub-packages


# Packages
# must have a value set for __path__
#     empty -> not a package


# Modules do not have to be entities in the file system..
# Typically they are


# Packages represent a hierarchy of modules/packages
# This does not necessarily relate to a file system hierarchy
# pack1.mod1
# pack1.pack1_1.mod1_1



# the importer will:
#     import pack1
#     import pack1.pack1_1
#     import pack1.pack1_1.module1
# import pack1.pack1_1.module1


# the sys.moldules cache will contain entries for:
#     pack1
#     pack1.pack1_1
#     pack1.pack1_1.module1
# However the namespace where the import was run will just contain:
#     pack1


# Lookup PEP302
# File based packages and modules is the most useful case


# The package paths are created using the file system dirs and files
# In file system packages are represented using a directory
# dir name becomes the package name
# the dir does not contain code.. so the code for the package goes into __init__.py
# This combination of dir and __init__ make up the package module


# For file based packages
#     create a dir who's name is the package
#     create a __init__
#     this dir is now treated as a package



# What happens when a file based package is imported
# pack1 is identified as a package

# app/
#     pack1/
#         __init__.py
#         module1.py
#         module2.py

# import pack1
#     the code in __init__ is executed
#     the module is cached in sys.modules with key pack1
#         it's just a module

#     packages have a __path__ property: file system dir abs path
#       like modules packages have a __file__ property -> abs path to the __init__ file



# Nested packages - packages that contain packages
# app/
#     module.py
#     pack1/
#         __init__.py
#         module1a.py
#         module1b.py
#         pack1_1/
#             __init__.pu
#             module1_1a.pu
#             module1_1b.pu

# dotted pack notation
# pack1.module1a
# pack1.pack1_1
# pack1.pack1_1.module1_1a



# Module
#     __file__      - abs path of the module code
#     __package__   - is the package the code is located in (is "" if the module is in the app root)
#                       e.g pack1, pack1.pack1_1

# Packages
#     __path__      - abs path of the package in the file system




# What gets loaded during the import phase
#     import pack1.pack1_1.module1_1a
#     at the very LEAST
#         pack1      is imported and added to sys.modules
#         pack1_1    is imported and added to sys.modules
#         module1_1a is imported and added to sys.modules

# but modules can import other modules
# if
# pack1/__init__ has imports to import pack1.module1a and import pack1.module1b
# then
# import pack1.pack1_1.module1_1a
#         pack1      is imported and added to sys.modules
#         pack1_1    is imported and added to sys.modules
#         module1_1a is imported and added to sys.modules
#               ALSO now in sys.modules
#         module1a   is imported and added to sys.modules
#         module1b   is imported and added to sys.modules




