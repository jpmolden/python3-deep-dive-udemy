

# First Class Objects
#     Can be passed to a function
#     Can be returned from a function
#     Can be assigned to a variable
#     Can be Stored in a Data Structure:
#         (such as lists, tuples, dictionary, set)

print('*** Example First Class Objects ***')
print('\tint, float, string, tuple, list')
print('\tAlso functions are first class Objects')


print('\n*** Higher Order Functions ***')
print('\tTakes a function or returns a function')

print('\n*** In this Section ***')
print('\tfunction annotations')
print('\tlamda expressions')
print('\tcallables')
print('\tfunction introspection')
print('\tbuilt-in higher order functions (sorted, map, filter)')
print('\tthe functools module (reduce, all, any)')
print('\tpartials, partial method')


print('\n*** Docstrings ***')

def my_func(a):
    """This is an example docstring
    Inputs:
        a: Does Somthing
    Returns:
        The other thing
    """
    return a

print(my_func.__doc__)


print('\n*** Function Annotations ***')
print('\tDoes not change how python runs or ristrict types in any way')
def my_func2(a: str, b: [1,2,3]) -> "A number":
    pass


print('\n*** Default Values with Function Annotations ***')
def my_func3(a: str = 'xyz',
            *args: 'Additional parameters',
            b: int = 1,
            **kwargs: "Additional keyword only params") -> str:
    print(a, args, b, kwargs)
    pass


print('\tAnnotations are stored in the annotations dictionary, metadata attached to the parameters')
print("\t", my_func3.__annotations__)
print('\tThese don\'t affect code at all they only help document code')
print('\tSee Sphinx')
print('\tType hints are >3.5 onwards, builds on annotations')












