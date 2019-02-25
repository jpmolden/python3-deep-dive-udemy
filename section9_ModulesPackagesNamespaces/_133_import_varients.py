import sys
import pprint

print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} What keys(modules) are in sys.modules {'*' * 20}")
for k in sorted(sys.modules.keys()):
    print("\t", k)
print(f"{'==' * 20}")

print(f"\tcmath in globals          {'cmath' in globals()}")
print(f"\tcmath in sys.modules      {'cmath' in sys.modules}")


print(f"\n\n{'==' * 20}")
from cmath import exp
print("\t** importing exp from cmath **")
print(f"\tcmath in globals now?     {'cmath' in globals()}")
print(f"\tcmath in sys.modules      {'cmath' in sys.modules}")
print(f"\texp in globals            {'exp' in globals()}")
print('\t', exp(2+2j))
# Putting cmath into the globals
cmath = sys.modules['cmath']
print('\t', cmath.exp(2+2j))
# The other cmath functions are also now in the globals
print('\t', cmath.sin(2+2j))
print('\t', cmath.sin(2+2j))
print(f"{'==' * 20}")


print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} overriding some globals {'*' * 20}")
from cmath import *
from math import *
pprint.pprint(globals())
# This will now fail because the math imports do not handle complex sin
# print('\t', sin(2+2j))
print(f"{'==' * 20}")
#


#
#
#
print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} performance of from vs import {'*' * 20}")
from time import perf_counter
from collections import namedtuple
Timings = namedtuple("Timings", 'timing1 timing2 abs_diff rel_diff_perc')
def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100
    timings = Timings(round(timing1, 1),
                      round(timing2, 1),
                      round(timing2 - timing1, 1),
                      round(rel_diff,2))
    return timings

print(compare_timings(1, 2))
test_repeats = 10_000_000
# Timing using the fully qualified module.symbol
import math
start = perf_counter()
for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start
print(f"Time with indirect symbol name (math.sqrt)  : {elapsed_fully_qualified:.2f} seconds")

from math import sqrt
start = perf_counter()
for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start
print(f"Time with direct symbol name(sqrt)          : {elapsed_direct_symbol:.2f} seconds")
print(f"Differences {compare_timings(elapsed_fully_qualified, elapsed_direct_symbol)}")
# Over 10M iterations there is virtually no difference in timing
print(f"{'==' * 20}")
#


#
#
#
print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} timing using a function wrapper {'*' * 20}")
import math
def func():
    math.sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()

end = perf_counter()
elapsed_func_indirect_symbol = end - start
print(f"Time with a wrapped function indirect (math.sqrt)   : {elapsed_func_indirect_symbol:.2f} seconds")
# Over 10M iterations there is a slight reduction in performance
from math import sqrt

def func():
    sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()

end = perf_counter()
elapsed_func_direct_symbol = end - start
print(f"Time with a wrapped function direct (sqrt)          : {elapsed_func_direct_symbol:.2f} seconds")
print(f"Differences {compare_timings(elapsed_func_indirect_symbol, elapsed_func_direct_symbol)}")
print(f"{'==' * 20}")
#


#
#
#
print(f"\n\n{'==' * 20}")
print(f"{'*' * 20} timing with nested imports {'*' * 20}")
def func():
    import math
    math.sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()

end = perf_counter()
elapsed__nestd_func_indirect_symbol = end - start
print(f"Time with a nested import function indirect (math.sqrt)       : {elapsed__nestd_func_indirect_symbol:.2f} seconds")
# Over 10M iterations there is a slight reduction in performance

# MUCH SLOWER!!! WHY? Because the it has to also add the sqrt to local namespace every iteration
def func():
    from math import sqrt
    sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()

end = perf_counter()
elapsed_nested_func_direct_symbol = end - start
print(f"Time with a nested import function direct (sqrt)               : {elapsed_nested_func_direct_symbol:.2f} seconds")
print(f"Differences {compare_timings(elapsed__nestd_func_indirect_symbol, elapsed_nested_func_direct_symbol)}")
print(f"{'==' * 20}")




