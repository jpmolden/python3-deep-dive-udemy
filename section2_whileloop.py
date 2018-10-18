
i = 0


# Python does not have do...while.. but
# while i < 5:
#     print(i)
#     i += 1
#


# Do while eqivilent
# i = 5
# while True:
#     print(i)
#     if i >= 5:
#         break


print("\n\n**** ****\n\n")

## Pattern 1
min_len = 2
name = input("Please answer your name: ")
while not(len(name) >= min_len and name.isprintable() and name.isalnum()):
    name = input("Do that again!!!: ")

# Prints out with substitution
print("Hello, {0}, your a {1}".format(name.upper(),name.lower()))


# Alternate pattern
min_len = 2
while True:
    name = input("Please answer your name: ")
    if (len(name) >= min_len and name.isprintable() and name.isalnum()):
        break

Prints out with substitution
print("Hello, {0}, your a {1}".format(name.upper(),name.lower()))


# Continue - Bails out of the current iteration but not the loop
a = 0
while a < 10:
    a += 1 # Increment
    if a % 2 == 0:   # In python false = 0, true is any integer
        continue
        print(a)


# Without Else Statement
l = [1,2,3]
val = 10

idx = 0
found = False

while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)
print(l)


# Else Statement
# If the while completes without terminating it executes the else!!! Useful
# Because there is no need for a flag..
# Suprising because you wouldn't expect the while/for to have an else
l = [1,2,3]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)






