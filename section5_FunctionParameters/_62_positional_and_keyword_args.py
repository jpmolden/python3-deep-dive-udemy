

print('\tPositional Arguments can be made optional by specifying a default value')


# Must specify default values after the first default argument
def my_func(a, b=100, c=None):
    print("\ta={0}, b={1}, c={2}".format(a, b, c))
    pass


my_func(1)
my_func(1,3)
my_func(1,435,44)


print('\t\n*** Using keyword arguments ***')
my_func(a=23, c=243)
print('\t\n*** Using a mix of posistional and keyword args ***')
my_func(23, c=243)


def my_func2(a, b, c):
    print("\ta={0}, b={1}, c={2}".format(a, b, c))
    pass


print('\t\n*** Calling with named args ***')
my_func2(10,20,30)
my_func2(b=10, a=23, c=22)
print('\t\n*** Once you use a named arg, all args after must also be named ***')
# Fail my_func(a=32, 10, 20)
# Fail my_func2(10, 20, a=22) - Cannot give multiple args for same parameter
my_func(1, c=4)






