

# Unpack iterable


# Unpacks a, b, c
def func(a, b, c):
    print("\n** func")
    print(a)
    print(b)
    print(c)
    pass


l = [10,20,30]
# Unpacking list before passing to function
func(*l)


# Similar when pos args passed to a function except we end up with a tuple
# The * operation unpacks the rest
def func1(a, b, *args, s):
    print("\n** func1")
    print(a)
    print(b)
    print(args)
    print(s)
    pass


# *args - the args name is just customary
func1(2,2,456,"wsd", s=54)
func1(2,2,456,"wsd", s="df")

def func2(a, b, *args, d):
    print("\n** func1")
    print(a)
    print(b)
    print(c)
    print(d)
    pass

func1(2,2,456,"wsd", 34, s=None)



def avg(*args):
    print(args)
    count = len(args)
    total = sum(args)
    return count and total/count
    # if count == 0:
    #     return 0
    # else:
    #     return total/count
    #     print(total/count)

print("Avg:", avg())

# Require 1 pos argument
def avg(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count

print("Avg:", avg(12))






