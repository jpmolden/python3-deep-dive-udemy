import datetime
# from builtins import dict

def my_func(a,
            b,
            c):
    print(a,b,c)


print(datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"))
# List with multiline comments
a = [1,2,3]

a = [1,  #comment
    2,
    3]


for i in a:
    print(i)
# Tuples
tup = (1,2,3,3)

print("Tuple: ", tup)
# Dict

dict = {'key1': 1,
        'key2': 2}
print("Dictionary", dict)

# Call Function
my_func("F",2,3)
