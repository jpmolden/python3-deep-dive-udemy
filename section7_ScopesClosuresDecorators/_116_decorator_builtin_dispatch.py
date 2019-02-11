from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from html import escape

print('\t')
print('\n*** Using the std library singledispatch decorator for single dispatch generic functions ***')
print('\tBe careful with strings, the dispatcher picks the closest match eg str is closer than Sequence')

# This becomes the default dispatch function
@singledispatch
def htmlize(a):
    return escape(str(a))

print(htmlize.registry)
print(htmlize.dispatch(str))

@htmlize.register(Integral)
def htmlize_integral_number(a):
    return "{0}(<i>{1}</i>".format(a, str(hex(a)))

# What is the registry now and how will it dispatch an int
print(htmlize.registry)
print(htmlize.dispatch(int))
print(htmlize.dispatch(bool))


@htmlize.register(Sequence)
def html_sequece(l):
    items = ("<li>{0}</li>".format(htmlize(item))
             for item in l)
    return "<ul>\n" + "\n".join(items) + "\n</ul>"


print(htmlize([1,3,4]))
print(htmlize((1,2,3)))
print('\tProblem: Strings are also sequence types')
print('\tThis will cause a recursion overflow error - Infinite loop!!!')
# print(htmlize("Python"))

for s in "Python":
    # A string is a sequence whose individual char are also strings!!
    print(type(s))

# Solution handle strings
@htmlize.register(str)
def html_str(s):
    return escape(s).replace("\n", "<br/>\n")


print(htmlize("Python 1 < 100 !>"))
print('\tA string is also a sequence, the registry lookup finds the closest match'
      'i.e str is less generic than Sequence so it using the str registry function')

# Lets say we want something more specific for tuple
@htmlize.register(tuple)
def html_tuple(t):
    items = (escape(str(item)) for item in t)
    return "({0})".format(", ".join(items))

print(htmlize([1,2,3]))
print(htmlize((10,20,30)))

# When using single dispatch, once registered the labels(functions) are not needed ie.
@singledispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(Integral)
def _(a):
    return "{0}(<i>{1}</i>".format(a, str(hex(a)))


@htmlize.register(str)
def _(s):
    return escape(s).replace("\n", "<br/>\n")


@htmlize.register(tuple)
def _(t):
    items = (escape(str(item)) for item in t)
    return "({0})".format(", ".join(items))

# Here the function names do not matter once registered
print(htmlize([1,2,3]))
print(htmlize((10,20,30)))
print(htmlize.registry)
# each of there _ functions have a separate memory address for each function object

a, *_, c = 1,2,3,4,5
print(a)
print(_)
print(c)
# by convension _ or __ means don't care about the name


