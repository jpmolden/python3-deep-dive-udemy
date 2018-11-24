from pprint import pprint

def my_func(a: "mandatory pos arg",
            b: "Optional positional" = 1,
            c=2,
            *args: "Extra positional",
            kw1,
            kw2=100,
            kw3=300,
            **kwargs: "Extra awargs here") -> "Does nothing":
    """my_func: Docstring here
    Return: None
    """
    i = 10
    j = 20
    return None


print(my_func.__doc__)
print(my_func.__annotations__)

print('\n*** Adding function(object) attributes ***')
my_func.short_desc = "A short description here"

pprint(dir(my_func), indent=4)
print(my_func.__name__)


# dummy code
i = 100

# TODO: Fix this function
def func_call(f):
    print("\tFunction id:", id(f))
    print("\tFunction name:", f.__name__)
    print("\targs defaults:", f.__defaults__)
    print("\tkw defaults:", f.__kwdefaults__)
    print("\tCode Object:")
    pprint(dir(f.__code__), indent=12)
    # print the code obj variable names including function scope vars
    print("\tVar names:", f.__code__.co_varnames)
    print("\tPositional Arg count:", f.__code__.co_argcount)

func_call(my_func)


print('\n*** Using the inspect module ***')
import inspect
from inspect import isfunction, ismethod, isroutine, getsource, getmodule

print(isfunction(my_func))
# methods are bound to a class or object
print(ismethod(my_func))


class My_class:
    def f(self):
        print("Do somthing")
        pass

print(isfunction(My_class.f))
print(My_class.f(My_class))

print('\tCreate a class instance')
my_obj = My_class()
print('\tMethods are functions that are bound of instances of a class, they are not functions')
print(isfunction(my_obj.f))
print(isroutine(my_obj.f))

print('\n*** Getting the source code ***')
print(getsource(my_func))

# Get the comments ouside the function, just before the definition
print(inspect.getcomments(func_call))
pprint(dir(inspect.signature(my_func)), indent=4)
print(inspect.signature(my_func).return_annotation)


print('\n*** Inspecting the signature ***')
sig = inspect.signature(my_func)
pprint(sig.parameters)

for k, v in sig.parameters.items():
    print(k,type(v))


for param in sig.parameters.values():
    print("name:", param.name)
    print("Default:", param.default)
    print("Annotation:", param.annotation)
    print("Kind:", param.kind)
    print("---------------------")


help(divmod)
def abs(a, b):
    pass

# help(divmod)
# Help on built-in function divmod in module builtins:
# divmod(x, y, /)  *** Here the slash means x, y are positional only!!
# i.e cannot use divmod(x=2, y=3), because the / says it is positional only
# We cannot define functions in this way, python can...



