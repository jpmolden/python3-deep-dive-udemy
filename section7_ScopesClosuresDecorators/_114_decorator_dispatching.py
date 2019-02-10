from builtins import type

print('\t*** In other languages overloading of functions happens when a function has '
      'multiple possible signatures'
      'this does not happen in python, (no static typing -> no function signature ***')

print('\n*** Single dispatch generic functions ***')


print('\n\t Application Format HTML data ***')
# HTML escaping of strings
from html import escape


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return "{0}(<i>{1}</i>".format(a, str(hex(a)))


def html_real(a):
    return "{0:0.2f}".format(round(a, 2))


def html_str(s):
    return html_escape(s).replace("\n", "<br/>\n")


def func1():
    func2()

def func2():
    print("It's ok to reference a funtion that isn't defined,"
          "as long as it's defined by the time it is executed!")

func1()



def html_list(l):
    # Write a generator
    # Dont use a loop to concatenate strings, use generators
    items = ("<li>{0}</li>".format(htmlize(item))
             for item in l)
    return "<ul>\n" + "\n".join(items) + "\n</ul>"

def html_dict(d):
    # Write a generator
    # Dont use a loop to concatenate strings, use generators
    items = ("<li>{0}={1}</li>".format(html_escape(k), htmlize(v))
             for k, v in d.items())
    return "<ul>\n" + "\n".join(items) + "\n</ul>"

def html_set(arg):
    return html_list(arg)


# print(html_str("""This is a multi line
# string with special chars 10 < 1000"""))
#
# print()
# print(html_int(100))
#
# print()
# print(html_escape(3.2 + 10j))
#

print('\n*** Writing a dispatcher ***')
from decimal import Decimal
# This isn't the best way since there are other generic integral types
# There are called abstract base classes, think of them as interfaces
def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    elif isinstance(arg, set):
        return html_set(arg)
    else:
        return html_escape(arg)

print('\tUsing HTMLize - Single dispatch generic function')
print(htmlize(100))
print()
print(htmlize("12213"))
print()
print(htmlize({10: "sfd", 20: 10}))
print()
print(htmlize([1,2,3]))
print()

#
print(htmlize(["""Python
rocks! 0 < 1""",
               (10, 20, 30),
               100]))


print('\n*** Create a slightly better way registry of types  ***')

def htmlize(arg):
    registry = {
        object: html_escape,
        int: html_int,
        float: html_int,
        Decimal: html_int,
        str: html_str,
        list: html_list,
        tuple: html_list,
        set: html_set,
        dict: html_dict,
    }
    fn = registry.get(type(arg), registry[object])
    return fn(arg)

print(htmlize(100))
print(htmlize([1,2,3]))


print('\n*** Create an even better way using closures and decorators ***')
print('\tCreate a way to modify the registry from outside')






