

# C Style iteration for(int i = 0; i < 5; i++) { ... }

# In python, an iterable is an OBJECT capable of returning values one at a time

# Iterable objects:
#     lists
#     tuples
#     strings
#

i = 0
while i < 5:
    print(i)
    # runs after each iteration
    i += 1

# Take the i variable out of scope
# i = None
# print(i)


# Range(5) is and iterable object
# For iterates an iterable not a list
for i in range(5):
    print(i)


print("{0} is an int".format(i))


# Here the list is an iterable object
for i in [1,2,3,4,5]:
    print(i)

# Strings are iterable
for c in 'hello':
    print(c)

# Tuples are iterable
for x in ('a','b','c',434):
    print(x)


print("\n ** Tuples are iterable")
for x in [(1,2), (3,4), (2,5)]:
    print(x)

print("\n ** Tuples are iterable")
# Unpacking of the tuple with i and j
for i,j in [(1,2), (3,4), (2,5), (2,3), ('d','e')]:
    print(i," ",j)

print(('2', '2', '3'))

for i in range(45):
    if i % 30 == 0 and i != 0:
        print(i)
        break


for i in range(1,4):
    print(i)
    if i % 7 == 0:
        print("Multiple of 7 found")
        break
else:
    print("NO Multiples of 7 found in range")
    # The else runs if the loop completes


print("\n ** Ranges are iterable")
for i in range(1,7):
    print("---- loop iteration START ----")
    try:
        # print("Somthing to try")
        10 / (i-2)
    except ZeroDivisionError:
        print("ERROR: Divide BY ZERO")
        continue
    finally:
        print("Will always run even if there is a break/continue")

    print(i)
    # print("---- loop iteration END ----")



# A string is iterable and has an index ie s[3]
# KEY Idea: NOt all iterables have an index ie sets, dicts, but are still iterable
# There is no concept of order here but they are iterable
s = "MY String"
for c in s:
    print(s[1])
#     prints the M char


print("\n ** BAD Idea with index based iteration")
# BAD IDEA
s = "Hello"
i = 0
for c in s:
    print(i, c)
    i += 1


print("\n ** Better idea with index based iteration")
# GOOD Idea: Use Indexing
for i in range(len(s)):
    print(i,s[i])


print("\n ** Better idea with index based iteration")
# Enumerate returns a tuple saves time and is quicker to eas and understand
for i, c in enumerate(s)
    print(i, c)




