import datetime


# from builtins import dict

def my_func(a,
            b,
            c):
    print(a, b, c)


print(datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"))
# List with multiline comments
a = [1, 2, 3]

a = [1,  # comment
     2,
     3]

for i in a:
    print(i)
# Tuples
tup = (1, 2, 3, 3)

print("Tuple: ", tup)
# Dict

my_dict = {'key1': 1,
        'key2': 2}
print("Dictionary", my_dict)

# Call Function - Positional Args
my_func("F", 2,
        30)

# Comparision operators
m1 = 22
m2 = 32
m3 = 34

print("comparison with line continuation \ ")
if m1 > m2 \
        and m2 < m3:
    print("true")
else:
    print("false")

# Multi line string (tabs and newlines will print
mystr = """This
    is
    a
    multi-line strinf"""

print(mystr)
