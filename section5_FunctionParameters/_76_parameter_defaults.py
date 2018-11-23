
# When a module is loaded
# All the code is executed right away

# The def is executed, func points to the function object in memory

a = 10

# Default values are also created as an object once def is fun, (not the func itself)
def func(a=10):
    print(a)


# default already created by the def
# func()

from datetime import datetime
# Approach 1 - Use current dt when the def is run
def log(msg, *, dt=datetime.utcnow()):
    # dt evaluated when def runs not when the function runs
    print("{0}, {1}".format(dt, msg))

log("message 1")
log("message 1", dt="1998-01-02")
log("message 2")

# N.B Message 2 will display EXACTLY SAME dt as message 1, dt default set at def not func execution


# Solution to the default param problem
def log(msg, *, dt=None):
    # dt evaluated when def runs not when the function runs
    # if dt is truthy return dt otherwise get datetime
    dt = dt or datetime.utcnow()
    print("{0}, {1}".format(dt, msg))


print("\n*** Using none in default ***")
log("message 1")
log("message 1", dt="1998-01-02")
log("message 2")
print("\tN.B - Message 2 has a different value now")
print("\tThe end result is that a kwarg can be optional and evaluated at func runtime not definition")


print("\n*** In general, beware of using a mutable object or callable for an argument default")

my_list = [1,2,3]

def func(a=my_list):
    print(a)


func()
func([4,5,6])
my_list.append(10)
# my_list is a mutable object and as a defualt arg a is referencing it
# if my_list changes then the result changes also
func()

# Tuples are immutable
my_tuple = (1,2,3)
def func(a=my_tuple):
    print(a)

func()
func([7,8,9])
# Tuples are immutable
# my_tuple.append(10)

print("*** Functions with default args set to mutable object are mutable!! If the list changes so does the default arg")
print("*** Use tuples to avoid this")







