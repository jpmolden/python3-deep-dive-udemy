# Using compule and exec to see how python import modules
# The compile function compiles into a python byte code object
# The exec funct is used to execute a code object

# Build a path to locate mod 1 src
import os.path
# Build a module
import types
# Load module into sys modules
import sys

# Does not need to match file name
module_name = 'moduleimportexample'
module_file = 'module1_source.py'
module_path = '.'


module1_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module1_rel_file_path)

# Read src code from file
with open(module1_rel_file_path, 'r') as code_file:
    source_code = code_file.read()


# create module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# Seyt a ref in sys modules
sys.modules[module_name] = mod

# complete setup - compile source code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

# execute module - use the module dict for the functions, classes ect (symbols)..
# Run code and put everything into the dict
exec(code, mod.__dict__)


# Done

mod.hello()

print(globals())

# We added the module to sys modules
# When python is running the sys modules contains a ref to to moduleimportexample,
# so it can be imported into the globals()
import moduleimportexample
moduleimportexample.hello

print(globals())
