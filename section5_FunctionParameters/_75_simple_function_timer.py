

def calc_hi_lo_avg(*args, log_to_console=False):
    # Bool Short Circuit
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    avg = (hi + lo) / 2
    if log_to_console:
        print("High={}, Low={}, Avg={}".format(hi,lo,avg))
    return avg


calc_hi_lo_avg(132,132,457,7,5,1,0,log_to_console=True)


import time


def time_it(fn, *args, rep=1, print_console=False, **kwargs):
    print("\n*args                  :", args)
    print("**Kwargs               :", kwargs)
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)

    end = time.perf_counter()
    if print_console:
        print("Took {} seconds".format((end - start) / rep))
    return (end - start) / rep

# time_it picks up and passes allong all the args to fn and all the kwargs apart from rep and print_console
time_it(print, "arg1", "args2", sep=" , ", end=" ***\n", rep=5, print_console=True)



def compute_powers(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

print(compute_powers(2, end=20))


# Using list compehension
def compute_powers_2(n, *, start=1, end):
    return [n**i for i in range(start, end)]

print(compute_powers_2(2, end=20))


# Using generators
def compute_powers_3(n, *, start=1, end):
    # using generator expression
    return (n**i for i in range(start, end))

print(list(compute_powers_3(2, end=20)))



# Using Timing
print("Using compute_powers")
time_it(compute_powers, 2, start=0, end=20000, rep=5, print_console=True)
print("Using compute_powers_2")
time_it(compute_powers_2, 2, start=0, end=20000, rep=5, print_console=True)
print("Using compute_powers_3")
time_it(compute_powers_3, 2, start=0, end=20000, rep=5, print_console=True)

# Generators compute contents as they are requested
a = (2**i for i in range(10000))
print(a)



