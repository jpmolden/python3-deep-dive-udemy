
# a good approach is to not return a list if it is mutated

def add_items(name, quantity, unit, grocery_list):
    grocery_list.append("{0} ({1} {2})".format(name, quantity,unit))
    return grocery_list

store1 = []
store2 = []
add_items('apples', 2, 'boxes', store1)
add_items('berries', 23, 'pounds', store1)
add_items('cheese', 1, 'wedges', store1)
add_items('python', 2, 'med rare', store2)
print("Store1 - ", store1)
print("Store2 - ", store2)


def add_items(name, quantity, unit, grocery_list=[]):
    grocery_list.append("{0} ({1} {2})".format(name, quantity,unit))
    return grocery_list


del store1
del store2
store1 = add_items('apples', 2, 'boxes')
add_items('milk', 2, 'gallons', store1)
store2 = add_items('python', 1, 'cooked')
print("\n*** Be Very careful when creating mutable default args to funcs")
print("Store1 - ", store1)
print("Store2 - ", store2)
print("Are they the SAME lists?", store1 is store2)
print("They are the SAME, why? Because the list reference is created at def_time!!!")



print("\n*** Do NOT use mutable default arg types in the function def, use NONE")
print("\tDefault type references are created ONCE when the def runs")
def add_items(name, quantity, unit, grocery_list=None):
    if grocery_list is None:
        grocery_list = []
    grocery_list.append("{0} ({1} {2})".format(name, quantity,unit))
    return grocery_list


del store1
del store2
store1 = add_items('apples', 2, 'boxes')
add_items('milk', 2, 'gallons', store1)
store2 = add_items('python', 1, 'cooked')
print("\n*** Be Very careful when creating mutable default args to funcs")
print("Store1 - ", store1)
print("Store2 - ", store2)
print("Are they the SAME lists?", store1 is store2)
print("They are the DIFFERENT!, why? Because the list is created at execution time!!!")

print("Bottom Line: Be careful using mutable object types with default args")


# Using standard approach
def factorial(n):
    if n < 1:
        return 1
    else:
        print("Calculating {0}!".format(n))
        return n * factorial(n-1)

factorial(3)
factorial(3)

# Using a cache
cache = {}
def factorial(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print("Calculating {0}!".format(n))
        result = n * factorial(n-1, cache=cache)
        cache[n] = result
        return result

cache = {}
factorial(5, cache=cache)
factorial(7, cache=cache)

print(cache)

print("A better technique is to use closures and decorators...")





