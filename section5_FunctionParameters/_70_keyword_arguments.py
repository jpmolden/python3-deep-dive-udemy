

# Can made a keyword argument required
def func(a, b, *args, kwarg1):
    print(a)
    print(b)
    print(args)
    print(kwarg1)


func(100, 12, "2", 456, 23456, 3, "2", kwarg1=1)


# No minimum pos args
def func(*args, kwarg1):
    print(args)
    print(kwarg1)


func(100, 12, "2", 456, 23456, 3, "2", kwarg1=1)

# Allowing no positional args
def func(*, kwarg1):
    print(kwarg1)

# Enforce keyword args
func(kwarg1=1)

# Putting it all together
def func(a, b=1, *args, d, e=True):
    print("\na is mandatory       :", a)
    print("b is optional          :", b)
    print("args optional          :", args)
    print("d mandaoty keyword arg :", d)
    print("e optional keyword arg :", e)


func(100, d=100)
func(100, 10, d=10)
func(100, 45, 1,2,3,4,5,7,8,9, d=10)
func(100, 45, 1,2,3,4,5,7,8,9, d=10, e=False)


# 2 Positional parameters the rest as keyword
def func(a, b, *, d):
    print("\na is mandatory        :", a)
    print("b is mandatory          :", b)
    print("No other args           :"   )
    print("d mandatory keyword arg :", d)


func(100, 10, d=10)


# Needs 1 pos argument, one optional pos arg, aditional *args, 2 kwd args d, e
def func(a, b=2, *args, d, e=15):
    print("\na is mandatory          :", a)
    print("b is optional           :", b)
    print("args                    :", args)
    print("d                       :", d)
    print("e optional with default :", e)

func(1,2,3,4,7,7,7,e=15, d=4)


func(11,'m/s', 's','t','a','r','a','r','g','s', d=None)







