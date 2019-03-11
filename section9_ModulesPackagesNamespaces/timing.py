# timing.py
"""
Times how long a snippet of code takes to run over multiple iterations
"""

print(f"loading timing.py: __name__ = {__name__}")
from time import perf_counter
from collections import namedtuple
# Allow us to pickup arguments from the command line
# goal to call python timing.py "code..." -r 10
import argparse

# Named tuple class
Timing = namedtuple("Timing", "repeats elapsed average")

def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)


if __name__ == '__main__':
    # Only see this if we execute the module directly
    # python timing.py
    # example use
    # python timing.py "[x ** 2 for x in range(10000)]" -r 10
    print(f"\n\n{'==' * 20}")
    print(f"{'*' * 20} Running as command line code {'*' * 20}")
    # get code, repeats from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code',
                        type=str, help="The python code snippet to time")
    parser.add_argument('-r', '--repeats',
                        type=int, default=10,
                        help="The number of times to repeat the test")
    # Parse the command line arguments into a namespace
    args = parser.parse_args()
    print(f"\ttiming this code          : {args.code}")
    print(f"\tthe number of repeats     : {args.repeats}")
    # print the timing results named tuple
    print("\t*** Timing results:", timeit(args.code, repeats=args.repeats))
    # We are able to call the module directly in the command line and do this but also
    # have the ability to import the module without running this code
    print(f"{'==' * 20}")



