
# Strings are immutable objects
my_var = "hello"


print(my_var, "\n*** String Function - Immutable")
print("my_var reference: ", hex(id(my_var)))
def process(s):
    print("Initial s: {0}".format(hex(id(s))))
    s = s + " world"
    print("Final s: {0}".format(hex(id(s))))
    return s

process(my_var)

# Scopes
#     Module scope
#     process() scope
#         my_var reference is passed to scope
#         s points to same point in memory
#         after, s points to new mem location
#         The function can't change the mem value...
#         .. but mutable may be unsafe

def process_list(lst):
    lst.append(100)

my_list = [1, 2, 3]
process_list(my_list)
print("\n*** Lists are mutable and so functions can mutate them, without a new reference ***")
print("my_list:\n\t" + my_list.__str__())

#     The function is passed a reference to a
#     mutable object, therefore it changes the
#     object without changing the mem location



def process_tup(t):
    t[0].append(3)

my_tuple = ([1,2], 'a')
print("\nTuples aren't mutable but the contents may be")
print("my_tuple:\n\t" + my_tuple.__str__())


print()