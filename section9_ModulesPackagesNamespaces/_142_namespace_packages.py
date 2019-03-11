# implicit namespace packages are package-like
# directories that may contain
#     modules
#     nested regular packages
#     nested namespace packages
#     CANNOT CONTAIN __init__.py

# the directories are implicitly made into there special types of packages

# PEP420


# Mechanics

# utils/
#     validators/
#         boolean.py
#         date.py
#     json/
#         __init__.py
#         serializers.py
#         validators.py


# Utils does not contain a __init__ and the same with validators
#     utils -> namespace package
#     validators -> namespace package
#     boolean.py -> module
#     json/ -> regular package


# Regular packages                       Namespace package
# type module                                 type modeule
# __init__ has code                           No code associated
# __file__ -> __init__ location               __file__ not set
# __path__ -> breaks if parent dir            paths -> dynamically
#             change and absolute                 (parent dir can change)
#             imports are used                    (import statement will need to change)
# single package lives                        single package can live in multiple
# in single dir                               no nested dirs. parts may live in a zip or outside project


# Example
# app/
#     utils/
#         validators/
#             boolean.py
#     common/
#         __init__.py
#         validators/
#             boolean.py

#                     (namespace pack)             (regular package)
#                     utils                         common
# type                module                        module
# __name__            utils                         common
# __repr__()       <module utils (namespace)>        <module common from '.../app/common'>
# __path__         _Namespace(['.../app/utils'])      ['../app/common']
# __file__            not set                            ../app/common/__init__.py
# __package__         utils                         common
# validators          utils.validators              common.validators


# # Importing
# Works just the same as with regular packages
# Cant flatten the namespace as with regular packages
# utils/
#     validators/
#         boolean.py
#         date.py
#         json/
#             __init__.py
#             serializers.py
#             validators.py
#
# import utils.validators.boolean
# from utils.validators import date
# import utils.validators.json.serializers


