

# Local, global, nonlocal, nested scopes
# Closures, closure scope
# Decorators, how they relate to closures, @

print('\n*** Closures are not lambdas ***')
a = 10
print('\tVariable is bound (reference) some object')
print('\tCant reference a everywhere')

print('\tName binding exists in the lexical scope or simply, scope')
print('\tBindings are stored in the namespaces')

print('\n*** The Global Scope ***')
print('\tspans a single file, NOT accross files')
print('\twith the exception of builtin scope(namespace) True, False, None, dict...')
print('\tGlobal scope are nested within the builtin scope')
print('\tModule 1 has its own scope, inside builtin')
print('\tPython will look in module namespace, then the builtin scope')


print('\n*** Using a module scope instead of builtin')
print = lambda x: "Hello {0}".format(x)
s = print("World!")
# Remove from namespace
del print

print(s)


print('\n*** The local scope ***')
print('\tFunctions also have their own scope')
print('\tVariables inside the function are not created untill the func is called')
print('\tA new scope is created when the function runs')


print('\n*** Nested scope ***')
print('\tLooks in local(function) scope first, then module scope, then builtin')
print('\tWhen requesting, will try to find the obj bound to the variable')


print('\tGlobal scope <-> Module scope')

a = 10

def my_func(b):
    print(True)
    print(a)
    print(b)

# Here a is a non local variable
my_func(200)

# Get another local scope
my_func('a')

a = []

def my_func():
    a.append(2)

# Here a is non local

my_func()
print(a)


print('\n*** Modifying the global from within the local? ***')

a = 0
def my_func():
    # A is local the = assigns it
    a = 100
    print("\t Local a = {}".format(a))

my_func()
print("\tA is now??!? = {}".format(a))
print('\ta MASKS the global variable a by the assignment')


print('\n*** The global keyword ***')

a = 100

def my_func():
    global a
    a = 1000

my_func()
print("a globally set to a = {}".format(a))



print('\n*** Global and Local Scoping ***')
print('\tWhen python encounters a function def at compile time it will')
print('\tScan for any labels (variables) that have values assigned to them')
print('\tIf the label has not been specified global, then it will be local')

print('\tVariable the are referenced but not assigned (eg True), then it look in')
print('\tenclosing scopes')

# eg
def func1():
    # At compile time, a is not assigned so it must be non-local
    print(a)

def func1():
    # Here a is assinged so it must be local
    a = 100

def func1():
    # Here python sees that a is in the global namespace
    # Python will create one in the global namespace if it does not exist
    global a
    a = 100

def func1():
    # Python knows a is local BUT it is used before assignment, therefore.. runtime error
    print(a)
    a = 100



a = lambda x, *args, **kwargs: True if x == 100 else False
a.__name__ = "This does stuff"
a._as = "df"


