

# ** is for dictionaries

# using 2 pos args, 1 kwarg, and **kwargs
def func(a, b, *, d, **kwargs):
    print("\na is mandatory          :", a)
    print("b is mandatory          :", b)
    print("d is mandatory kwarg    :", d)
    print("** Kwargs               :", kwargs)


func(1,2,d=100, e=10, f=45, g=7)
func(1,2, d=4)

# Using kwargs only
def func(**kwargs):
    print("\n** Kwargs               :", kwargs)

func(d=100, e=10, f=45, g=7)

func(d=4)


# Using kwargs only
def func(*args, **kwargs):
    print("\n*args                  :", args)
    print("**Kwargs               :", kwargs)


func(1,2,3,4,5,6,7,9,8,45,6456,"s", a=1, b="54", G=7, e=[1,2,3], f=(1,2), g={'a': 2, 'b': "2", 2: 23})
d = {23: 45, "3": 7, 12: 78, "23": "Done"}
for k, v in d.items():
    print(k, v)

print(1,2,3,sep="\n\t",end="\n")

