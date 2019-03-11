#
import math

# Create an alias
# math is added as a key in the sys.modules
# add the r_math symbol to the global namespace
# i.e math is not in the globals
# if the reference already exist in globals it is replaced
import math as r_math

# add sqrt to the globals namespace, referencing math.sqrt in sys.modules
from math import sqrt


# is math in sys.modules if not load the module to sys.modules
# add the symbol r_sqrt to globals and reference the math.sqrt
# math is not in the namespace
from math import sqrt as r_sqrt

# What changes is what is added to the globals namespace


# add "all" symbols defined in the math module to the globals namespace
# eg pi, sin.. math is not in globals
# The reference is overwritten if it already exists
from math import *


# *** Misconceptions ***
# using "from math import sqrt" is more efficient, it's not since python still loads the WHOLE module
# it only tells python what symbols are placed in the module 1 globals namespace


# "from <module> import *" can lead to bugs but it has it's uses (packages)


# "from cmath import *"
# "from math import *" - math also has an sqrt function so it is replaced in the globals
#     not always very safe


# Efficiency?
# import math
# vs from math import sqrt
# Very little difference for import

# When calling?
# calling, reference the math symbol - math.sqrt()
# calling, reference the sqrt directly - sqrt()
# 2 lookups vs just 1 - little difference

# aim for readability
# use import math.. for readability








