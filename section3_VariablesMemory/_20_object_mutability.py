

class My_account:
    def __init__(self):
        self._account_name = "New Account"
        self._balance = 1000

    def __str__(self):
        return "\n\t" + self._account_name + "\n\tBalance :" + str(self._balance)



# Mutable obects internal state can be changed.

A = My_account()
print("Account A: ", A)


# Immutable objects
#     int
#     float
#     bool
#     string
#     tuples
#     string
#     Frozen Sets
#     User Defined Classes (Can be mutable)

# Mutable objects
#     Lists
#     Sets (relates to sets
#     Dicts
#     User Defined Classes



# Immutable tuple, in this case both the tuple and int are immutable
# Contains references to immutable objects
t = (1, 2, 3)

# Lists are mutable
a = [1, 2]
b = [3, 4]

# Mixture of tuple and list
t = (a, b)

a.append(3)
b.append(5)

print(t)
# Immutable types can contain mutable types


my_list = [1, 2, 3]
print(type(my_list))
print(id(my_list))
my_list.append(4)
# Mem addr doesn't change
print(id(my_list))

my_list_1 = [1, 2, 3]
print(id(my_list_1))
# Concat of 2 objects creates a new object
my_list_1 = my_list_1 + [4]
print(id(my_list_1))

# Dicts are mutable
print("*** Dicts are mutable ***")
my_dict = dict(key1=1, key2='a')
print("\t", my_dict)
print("\t", id(my_dict))


print("\n*** tuples are immutable ***")
t = (1, 2, 3)
print("\t", t[0])
t = ([1, 2], [3, 4])
print("\tid(t)", id(t))
t[0].append(12)
print("\tHowever since a list is mutable t's contents are mutable:\n\t", t)











