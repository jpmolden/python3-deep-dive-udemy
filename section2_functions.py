# from math import sqrt
import math

s = [1,2,3]


print (math.sqrt(s[0]))
math.exp(s[1])


def func3():
    return func4()

def func4():
    return 'running func 4'



# def defines a function object location and metadata
# : is documentation only


def my_function(a:int = 34,b:int = 44):
    # print("Running function 1")
    return a * b

my_function()
# Print the function itself

print(my_function)
# Example of polymorphism

print (my_function('a',2))


print(func3())


def func5():
    return func6()

# Will cause error since this function is not defined yet
# func5()

def func6():
    return 1



# LAMDAS - Create function without a name but creates a function
# Inline annoymous functions
print(type(func5))

my_func = func5
print (my_func())
fn1 = lambda x: x**2
print(fn1(2))







