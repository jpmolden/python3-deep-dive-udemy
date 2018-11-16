# Peephole optimizer - pre calculates constants
# Some optimizations occur at compile time

# Constant expressions
#     24 * 60
#     Python will optimize to 1440 automagically

# Short sequences
#     of length < 20
#     (1, 2) * 5

# print((1, 2) * 5)


# Membership Tests
#         literal constant lists
#     if e in [1, 2, 3]
#      the list is transformed into a tuple (1, 2, 3)
#         list -> tuple
#         set  -> frozen set

#     Set membership is much faster than list or tuple membership
#         (set are implemented like dictionries)

#  ** Faster - use a set
#     if e in {1, 2, 3}

def my_func():
    # Python complies and may optimize
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    # More than 20 chars so will not peephole optimize
    d = 'ab' * 11
    e = "the quick brown fox" * 5
    f = ['a', 'b'] * 3

# Print the pre calculated constant expressions
print(my_func.__code__.co_consts)

print("\n*** Membership Tests ***")
def my_func_2():
    if e in {1, 2, 3}:
        pass

print(my_func_2.__code__.co_consts)

print("\n*** Set Membership is faster ***")
import string
import time
print(string.ascii_letters)
char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print(char_tuple)
# Sets are not ordered
print(char_set)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass

# Python is polymorphic, be concerned with properties (support for in)
start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print("\tChar list", end-start, "seconds")

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print("\tChar tuple", end-start, "seconds")

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print("\tChar set", end-start, "seconds")

# Set membership is much faster
