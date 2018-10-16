i = 0


# Python does not have do...while.. but
while i < 5:
    print(i)
    i += 1



# Do while eqivilent
i = 5
while True:
    print(i)
    if i >= 5:
        break


print("\n\n**** ****\n\n")

min_len = 2
name = input("Please answer your name: ")

while not(len(name) >= min_len and name.isprintable() and name.isalnum()):
    name = input("Do that again!!!: ")

