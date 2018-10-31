# Python memory manager, related to garbage collection
# Using the ctypes import to view the reference count for python objects to memory

# Reference to a mem address


import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value




if __name__ == "__main__":
    my_var = 10

    # How many other cariables are pointing to the same mem addr

    # Reference of my_var assigned to other_var
    other_var = my_var

    # Reference count now 2..

    del my_var
    del other_var

    import sys
    a = [1,2,3]
    # a points to a mem addr
    print((id(a)))


    # Always increases reference count by 1 by using this
    print("sys.getrefcount(a):", sys.getrefcount(a))




    # Id of a is evaluated first
    # Id finishes runninf and returns the mem addr and releases the ptr
    print("ref_count(id(a):", ref_count(id(a)))

    # Some integer mem reference
    # print("With the mem reference instead", ref_count(139721134255560))

    #
    b = a

    print("\nINFO: After a = b")
    print("id(a): ", id(a))
    print("ref_count(id(a):", ref_count(id(a)))

    c = a

    print("\nINFO: After c = a")
    print("id(a): ", id(a))
    print("ref_count(id(a):", ref_count(id(a)))


    c = 10

    print("\nINFO: After c = 10")
    print("id(a): ", id(a))
    print("ref_count(id(a):", ref_count(id(a)))


    b = None # B no longer references a, None is a object
    print("\nINFO: After b = None")
    print("id(a): ", id(a))
    print("ref_count(id(a):", ref_count(id(a)))


    a_id = id(a)
    a = None
    # Memory address reference is tossed
    print("\nINFO: After a = None")
    print("a_id: ", a_id)
    print("ref_count(a_id):", ref_count(a_id))
    print("...... May change, might not... as memory is freed up/allocated")
    jnfdvjn = "jnvdzfkjbnzfdkjnfzkjvfdjnvkjfznv"
    jnfdvjn = "dsfnjfdzvjzvnjd"
    jnfdvjn = [1,2,3,4]
    print("ref_count(a_id):", ref_count(a_id))
