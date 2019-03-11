from pprint import pprint

print(f"{'=' * 20}")
print(f"Running main.py module name {__name__}")
# __main__ is the starting point of wherever module we start

# The code for module1 does not happen untill this import. Execs the code and puts it into the sys.modules cache
import module1
# The pprint_dict will be part of the module1 globals which prints when we import module1

print(module1)
module1.pprint_dict('main.globals', globals())
import sys
pprint(sys.path)

# Print the system module cache
pprint(sys.modules)
# Importing modules multiple times does nothing as they are already in the sys.modules cache
# None of the module1 code will be run
import module1
import module1

del globals()['module1']
# module1 no longer in the namespace, the module is still in memory and is referenced
# by the sys.modules cache
# it's in cache but not in the global namespace
import module1
# The reference is brought back into the globals but the code isn't run again
module1.pprint_dict('main.globals', globals())

print(f"{'=' * 20}")
