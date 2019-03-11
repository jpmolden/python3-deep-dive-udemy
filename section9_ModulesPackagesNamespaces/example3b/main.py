import sys
# The importer execs the code
import importer

# Need a reference
# Create a module1
print(f"{'=='*40}")
print(f"{'*'*20} calling the import_ {'*'*20}")
module1 = importer.import_('module1', "module1_src.py", '.')
print(f"{'=='*40}")

# The importer has sets up where the module is from
print(f"sys says: {sys.modules.get('module1', 'module1 not found')}")
module1.hello()

print(f"\n\n{'*'*20} calling import for module2 {'*'*20}")
import module2
# If a module is already imported it does not rerun the code
module2.hello()

# The hard part is where the code comes from the src file.. anywhere.. a zip.. builtin..
# But the process is the same
print("\n\n\t1) Checks the sys.modules cache to see if the module has been imported")
print("\t2) if not it creates a new module object (types.ModuleType")
print("\t3) loads the src code")
print("\t4) adds an entry to sys.modules")
print("\t5) compiles and executes the src code")