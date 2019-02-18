data_dict = dict(key1=100, key2=100, key3=200)
# The key for a dict must be a hashable type


from collections import namedtuple
# The keys method returns an iterable of the keys
# In >=python3.6 the key order is preserved
# Prior to 3.6 it may not be
Data = namedtuple("Data", data_dict.keys())

print(Data._fields)

# NOT robust!!
d1 = Data(*data_dict.values())
# This way is only consistent in python 3.6
print(d1)


d2 = Data(key3=100, key1=12, key2=200)
print(d2)

# Using keyword unpacking is more robust
d2 = Data(**data_dict)

# Using the get attribute
key_name = "key2"
print(data_dict[key_name])
# won't work d2.key_name
print(getattr(d2, key_name))


# Getting a value or returning a default
print(data_dict.get('key1', None))
# Get attr has a positional default argument
print(getattr(d2, "key1", None))
print(d2.key1)


# Why do this
#     List of dict to list of named tuple
# data_rows[0]['date_imported']
# A better way
# data_rows[0].data_imported
#


#
# Example - list of dicts to lists of namedtuple
data_list = [
    {"key2": 1, "key1": 3},
    {"key1": 5, "key2": 4},
    {"key1": 1, "key2": 3, "key3": 7},
    {"key2": 3},
    {"key3": 100}
]
# Generate a list of named tuples
# Create a set of keys
keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)
print(keys)

# Using set comprehension instead
keys = {key for dict_ in data_list for key in dict_.keys()}

# Create a namedtuple
Struct = namedtuple("Struct", sorted(keys))
print(Struct._fields)
# Setup the defaults to None for all the keys

Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
# Convert each dict into a Struct namedtuple
tuple_list = []
for dict_ in data_list:
    # Unpack the dict into kwargs
    tuple_list.append(Struct(**dict_))
print(tuple_list)


def tuplift_dicts(dicts):
    """
    Converts a list of dicts to a list of named tuples

    :param dicts: list of dicts
    :return: list of namedtuple
    """
    keys = {key_ for dict_ in dicts for key_ in dict_.keys()}
    # sort the keys into a named tuple
    Struct = namedtuple("Struct", sorted(keys), rename=True)
    Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
    # using list comprehension
    # return a list of namedtuple
    return [Struct(**dict_) for dict_ in dicts]


print(tuplift_dicts(data_list))




