
# Some stings are interned (reuse objects on demand)

# As python code is compiled some identifiers are interned
#     variable names
#     function names
#     class names
#     ect..

# Some string literals may be automatically interned
#     'hello world'



# two equal string that will be interned
a = 'some_long_string'
b = 'some_long_string'


print("Since the string are the same they will be interned")
print("\tCompare with equality operator, a == b:", a == b )
print("\tCompare with equality operator, a is b:", a is b )


print("*** Not all string are interned by Python ***")


print("*** Can force interning ***")
import sys
a = sys.intern("the quick brown fox")

print("*** Useful where there is repetition, NLP ***")

def compare_using_equals(n):
    a = "a long string to be interned" * 200
    b = "a long string to be interned" * 200
    for i in range(n):
        if a == b:
            pass
    print("id(a):{0}, id(b):{1}".format(id(a), id(b)))

def compare_using_interning(n):
    a = sys.intern("a long string to be interned" * 200)
    b = sys.intern("a long string to be interned" * 200)
    for i in range(n):
        if a is b:
            pass
    print("id(a):{0}, id(b):{1}".format(id(a), id(b)))


import time

start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print("using interning", end-start)

# Interning forces python to optimize for these specific long string and use them as a shared reference
start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print("using Equals", end-start)
