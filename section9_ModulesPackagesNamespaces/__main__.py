# __main__.py

# This module will be called when we call the package with
# (venv) C:\uController\python3-deep-dive-udemy>python section9_ModulesPackagesNamespaces

# other uses of __main__
# make the app into a zipfile
# Zip the application
#   python -m zipfile -c my-app __main__.py timing.py
# View the files that have zipped
#   python -m zipfile -l my-app

#
# execute directly from the zipfile and python starts at the __main__.py file
#   python my-app
#
# results:
#   loading __main__.py: __name__ = __main__
#   loading timing.py: __name__ = timing
#   Result = Timing(repeats=1000, elapsed=0.376791011, average=0.00037679101100000003)

# We can zip and application and execute it, import from within a zipfile and more

print(f"loading __main__.py: __name__ = {__name__}")

import timing
# list comprehension
code = '[x ** 2 for x in range(1000)]'
result = timing.timeit(code, 1000)
print(f"Result = {result}")
# The timing module would also be useful if we could call it from the command line


