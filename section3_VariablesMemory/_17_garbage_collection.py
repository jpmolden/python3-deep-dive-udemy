# Python keeps track of number of references to an object.
# Python memory manager reclaims memory when the ref count is 0

from section3_VariablesMemory._16_reference_counting import ref_count as ref_count
# from section2_Basics.section2_Classes import Rectangle
#
# print(globals())
#
# x = Rectangle(12,12)
# print(x.to_string())


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


# Circular references
