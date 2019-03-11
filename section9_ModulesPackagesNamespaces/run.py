# run.py
print(f"loading run.py: __name__ = {__name__}")
# picks up the name of the module
import module_4
# Whatever module is the entry point for the program it's name is changed to __main__


import timing
# list comprehension
code = '[x ** 2 for x in range(1000)]'
result = timing.timeit(code, 1000)
print(f"Result = {result}")
# The timing module would also be useful if we could call it from the command line



print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} Using the zipfile package {'*' * 20}")
# Using the zipfile command line functionality:
# python -m zipfile -c app.zip module1.py run.py main.py
# python -m zipfile -l app.zip


# when we
# (venv) C:\uController\python3-deep-dive-udemy>python section9_ModulesPackagesNamespaces





