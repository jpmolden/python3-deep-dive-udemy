# Python keeps track of number of references to an object.
# Python memory manager reclaims memory when the ref count is 0

# from section2_Basics.section2_Classes import Rectangle
#
# print(globals())
#
# x = Rectangle(12,12)
# print(x.to_string())
# Circular references
import ctypes
import gc

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

def obj_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object Exists"
    return "Not Found"


# Circular references

obj_a = 20
obj_b = 10

# Circular Reference
obj_a = obj_b
obj_b = obj_a

my_var = obj_a

# Del my_var
print("ref_count(id(obj_a))", ref_count(id(obj_a)))

# gc, garbage collector is turned on by default
# Cleans up circular references
# can call manually

# gc doesn't always work in Python < 3.4
#         if a circular ref object has a __del__() dessructor
#         The order of destruction might be important
#           if a dBase or somthing ect.
#           object is marked as uncollecable


# Creating circular reference objects
class A:
    # Here self is an instance of A
    def __init__(self):
        # Pass instance of A to B constructor
        self.b = B(self)
        # Print out mem addr of the references
        print("A: self: {0}, .b: {1}".format(hex(id(self)), hex(id(self.b))))

class B:
    # the a argument is the self in the constructor above
    # self is instance of B
    def __init__(self, a):
        self.a = a
        print("B: self: {0}, .a: {1}".format(hex(id(self)), hex(id(self.a))))


# Don't want to clean un circular references for this example
gc.disable()
my_var = A()

print("hex(id(my_var)):     Points to A.self", hex(id(my_var)))
print("hex(id(my_var.b)):   Points to B.self", hex(id(my_var.b)))
print("hex(id(my_var.b.a)): Points to A.self.b.a == back to A.self", hex(id(my_var.b.a)))

print("\n*** Ref count of the circular objects A and B **")
a_id = id(my_var)
b_id = id(my_var.b)
print("\tref_count(a_id): ", ref_count(a_id))
print("\tref_count(b_id): ", ref_count(b_id))
print("\ta_id: ", obj_by_id(a_id))
print("\tb_id: ", obj_by_id(b_id))
print("\tDestroy one reference to A")
my_var = None
# A still points to B, B to A
print("\tref_count(a_id) =", ref_count(a_id), "and:", obj_by_id(a_id))
print("\tref_count(b_id) =", ref_count(b_id), "and:", obj_by_id(b_id))

print("** Collect Garbage **")
gc.collect()
print("\ta_id:", a_id)
print("\ta_id:", b_id)
print("\tref_count(a_id) =", ref_count(a_id), "and:", obj_by_id(a_id))

print("\tref_count(b_id) =", ref_count(b_id), "and:", obj_by_id(b_id))
print("\tref_count(a_id) =", ref_count(a_id), "and:", obj_by_id(a_id))



