print(f"\n\n{'*' * 10} What happens when we import modules {'*' * 10}")
# Imports happens dynamically
# Finding the module is the complex part

import sys
from pprint import pprint
#
pprint(f"Where is python installed: {sys.prefix}")
pprint(f"Where C binaries installed: {sys.exec_prefix}")
pprint(f"Where does python look for imports: {sys.path}")

# The mooule needs to be in the sys path
# Not recommended!!! Add modules to the sys path

#  How does python import modules
print("\n\n\t1) Checks the sys.modules cache to see if the module has been imported")
print("\t2) if not it creates a new module object (types.ModuleType")
print("\t3) loads the src code")
print("\t4) adds an entry to sys.modules")
print("\t5) compiles and executes the src code")

print("\nImportant!!! When a module is imported it's code is executed")


print(f"{'=' * 20}")
print("EXAMPLE 2 - hacking the sys.modules")
# Example when we import a module python first looks in the sys.modules
# Hack the sys.modules to place a k,v pair
# DO NOT DO THIS!!!!!!
# Add the name (a function!!) to the cache
sys.modules['test'] = lambda: "DO NOT DO THIS!! Testing module caching"
# looks for test in sys.modules
import test
print(test())
# DO NOT DO THIS!!!!!!
print(f"{'=' * 20}")

print(f"\n{'=' * 20}")
print("EXAMPLE 3 - compile and exec")
# The compilation compiles the src into python byte code
# The exec is ued to execute a code object
# We can tell















