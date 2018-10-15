

# convention (lead _ are considered "Private")
# No concept of private however
# Objects named in this way will not be imported with from module import *
from decorator import __init__

_my_var = "hello"


# Dunder used to "mangle" a class - in inheritance chains
__my_var


# Dunder beggining and end ** Special Meaning **
# __init__() special names

# DONT INVENT THEM
# x < y
# x.__lt__(y)


# Style nameing:

# Other Naming Conventions from the PEP 8 Style Guide
# Modules short, all-lowercase names. Can have underscores.
# Packages short, all-lowercase names. Preferably no underscores. utilities
# db_utils dbutils
# Classes CapWords (upper camel case) convention BankAccount
# Functions lowercase, words separated by underscores (snake_case) open_account
# Variables lowercase, words separated by underscores (snake_case) account_id
# Constants all-uppercase, words separated by underscores MIN_APR