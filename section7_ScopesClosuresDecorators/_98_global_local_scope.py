
a = 10

printt = print

from functools import partial
printtab = partial(print, "\t")
printtab.__doc__ = "A print with a leading tab, eqiv to print(\"\\t\", *args)"


def my_func(n):
    print("global a: ", a)
    c = a ** n
    print(c)

my_func(1)


print('\n*** When assigning, be careful ***')

def my_func(n):
    a = 20
    c = a ** n
    printtab(c)


print('\t locally a = 10 but in the function scope a = 20')
print('\tShadowed the outer scope variable')
my_func(10)


print('\n*** Using the global variable explicitly ***')
def my_func(n):
    global a
    a = 20
    c = a ** n
    printtab(c)


my_func(4)

def my_func():
    global var
    var = "hello World"
    printtab(var)

printtab("Global variable from the function")
my_func()
printtab("Global variable from the global scope")
printtab(var)


a = 10
def my_func():
    printtab("Global a =", a)


my_func()
a = 10
printtab("A problematic function, at compile time python knows the variable a is local")
printtab("In the local scope a cannot be found, referenced before assigment")
def my_func():
    printtab("Global a =", a)
    a = "hello"
    printtab(a)

# my_func()


printtab("Same with lambdas")
printtab("Functions are objects and have names")
print(True)
# Here python looks in global, then builtin

print("*** Python does not have code block scope, unlike java")

for i in range(10):
    x = 2 * i

print("i still exists here too!!!, watch out i =", i)
