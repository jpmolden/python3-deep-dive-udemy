import sys


print("=====================")
print("Running main.py - module name {0}".format(__name__))


# Imports can be wherever but are better placed at the top.
import module1

print(module1)

print("Importing module1 again")
import module1

# module1 is cached but not in the global namespace
# This does not remove the obj from memory
del globals()['module1']

# Module1 is still in the sys cache this add back to the globals namespace
import module1
print("=====================")


module1.pprint_dict("main globals", globals())

# Print the system cache
print(sys.path)

print(sys.modules['module1'])



# Do not try this