import os


print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} Create a module file and re-importing {'*' * 20}")

def create_module_file(module_name, **kwargs):
    """ Create a module file named <module_name>.py
    Module has a single function (print_values) that will print
    out the supplied (stringified) kwargs

    :param module_name:
    :param kwargs:
    :return:
    """
    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)
    with open(module_abs_file_path, 'w') as f:
        f.write(f"# {module_name}.py\n\n")
        f.write(f"print('\trunning {module_name}.py..')\n\n")
        f.write(f"def print_values():\n")
        for key, value in kwargs.items():
            f.write(f"\tprint('\t\t{str(key)}', '{str(value)}')\n")

create_module_file('test_module', k1=10, k2='python')
print("\timporting the test_module.. the code inside will run")
import test_module
# Overwrite the module!!! at runtime
create_module_file('test_module', k1=10, k2='python', k3='cheese', )
# Since this is already loaded into the sys modules it does not need to be reloaded
import test_module
import sys
# The module is in sys.modules
print("\ttest_module in sys.modules: ", "test_module" in sys.modules)
print(f"\tThe globals       test_module id is: {hex(id(test_module))}")
print(f"\tThe sys.modules   test_module id is: {hex(id(sys.modules['test_module']))}")
print(f"{'==' * 20}")
#
#


#
#
print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} Re-importing a module {'*' * 20}")
# Delete the existing reference
del sys.modules['test_module']
print("\ttest_module in sys.modules: ", "test_module" in sys.modules)
import test_module
print(f"\tThe globals       test_module id is: {hex(id(test_module))}")
print(f"\tThe sys.modules   test_module id is: {hex(id(sys.modules['test_module']))}")
# The module has a new address in memory
print(f"\tIs test_modules in the globals: {'test_module' in globals()}")
# This approach is problematic because name conflicts may occur
print(f"{'==' * 20}")
#
#


#
#
print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} Re-importing using importlib {'*' * 20}")
# Change the module again
create_module_file('test_module', k1=10, k2='python', k3='cheese', k4='parrots')
import importlib
# Keep the same memory address for the module in the sys.modules file. The sys.modules is mutated
importlib.reload(test_module)
# The memory address does not change, if the module is already referenced this is safer...
print(f"\tThe globals       test_module id is: {hex(id(test_module))}")
print(f"\tThe sys.modules   test_module id is: {hex(id(sys.modules['test_module']))}")
print(f"{'==' * 20}")
#
#


#
#
print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} Modifying a module .py at runtime {'*' * 20}")
# Create a new module
create_module_file('test_module_2', k1='python')
print("\timport the test_module_2")
from test_module_2 import print_values
# Modify the module again but don't reaload it
create_module_file('test_module_2', k1='not python')
# The compiled python byte code will still show python even though the file has changed
print_values()
# We don't have a handle
# importlib.reload(test_module_2)
# So use the handle from the sys.modules
importlib.reload(sys.modules['test_module_2'])
# Still prints the OLD VALUES!!!
print_values()
# One solution
# from test_module_2 import print_values
# Another solution
print_values = sys.modules['test_module_2'].print_values
print_values()
# Bottom line:
# Reloading is possible but not always safe!!
print(f"{'==' * 20}")



