

def fact(n):
    return 1 if n < 2 else n * fact(n-1)


results = map(fact, range(6))
# Map object - A generator!!!! in python3
print(results)
print(type(results))

for x in results:
    print(x)

# Will print nothing - map returns a generator!!
for x in results:
    print(x)



print('\n*** Map returns a generator ***')
l1 = [1,2,3,4,5]
l2 = [10,20,30]
l3 = [100,200,300,400,500,600]

results = list(map(lambda x,y,z: x+y+z, l1, l2, l3))
print(results)

results = map(lambda x,y: x+y, l1, l2, l3)
print(results)
# Calculation is deffered untill here!
# for x in results:
#     print(x)

x = range(25)
print(x)
for i in x:
    print(i)

print('\tUnlike map and filter the range can be reused')
x = list(filter(lambda x: x % 3 == 0, range(25)))

l = [0, -1, -2, 1+2j, 0+0j, '', 1,2,3,4,5,6,7, '\0', 'a', None, False, True, 3.14]

print("Items that are divisable by 3 using filter:", x)
x = list(filter(None, l))
print("Returning the truthy items in a list:", x)

x = list(filter(lambda x: not bool(x), l))
print("Returning the falsy items in a list:", x)


print('\n*** The zip function ***')
l1 = [1,2,3,4]
l2 = [10,20,30,40]
l3 = "Python"
results = zip(l1, l2, l3)
for x in results:
    print(x)
# Get nothing - zip is a Generator!!!
print("Generators can only be evaluated once!, prints nothing")
for x in results:
    print(x)

x = zip(range(1000), 'python')
print(list(x))



print('\n*** Using List Comprehensions ***')
l = range(10)
# map(fact, l)
# List all the factorials in
results = [fact(n) for n in range(100) if fact(n) < 10000]
# This creates a list not a generator, map may be better if all results not used
print(results)

# Create a generator instead
results = (fact(n) for n in range(100) if fact(n) < 10000)
print(results)

for i in results:
    print(i)

print("\nA generator will not run twice")
for i in results:
    print(i)



print('\n*** Using List Comprehensions ***')
l1 = [1,2,3,4,5,6]
l2 = [10,20,30,40]
print(list(map(lambda x,y: x+y, l1, l2)))
results = [x+y for x,y in zip(l1, l2)]
print("Results using zip and list comprehension {}".format(results))

# Use filter out the odd results
results = list(filter(lambda x: x%2==0, map(lambda x,y: x+y, l1, l2)))
print("Results using filter and map {}".format(results))

# Same result using list comprehension
results = [x+y for x,y in zip(l1, l2) if (x+y)%2 == 0]
print("Results using list comprehensions {}".format(results))

# Using a generator - Doesn't calc anything until requested!!
results = (x+y for x,y in zip(l1, l2) if (x+y)%2 == 0)
print(results)
for e in results:
    print(e)












