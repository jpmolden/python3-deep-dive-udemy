# impoerer
# Build a path to locate module1 src on the disk
import os.path
import types
import sys

# Typically the module name is the file name
print(f"Running {__name__}.py")

def import_(module_name, module_file, module_path):

    # Check if in already in modules
    if module_name in sys.modules:
        return sys.modules[module_name]

    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    # Read the src
    with open(module_rel_file_path, 'r') as code_file:
        src_code = code_file.read()

    # Create a module obj
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    # Set a reference in sys.modules dict
    sys.modules[module_name] = mod

    # Compile the src code
    # filename is just metadata
    code = compile(src_code, filename=module_abs_file_path, mode='exec')

    # execute the compiled src code
    # it hasn't run yet
    # Where do we want global stuff to go, what namespace
    # The module is just namespace (functions ect and addresses) in this case the hello func will
    # be in the mod dict

    # Part of the execution is to run the def hello, which puts hello into the global namespace
    # the mod.__dict__
    exec(code, mod.__dict__)

    return sys.modules[module_name]




