
a = 6
if a < 5 :
    print('a < 5')
else:
    print('a <= 5')


a = 10
if a < 5 :
    print('a < 5')
else:
    if a < 10:
        print("5 <= a < 10")
    else:
        print("a >= 10")




# Switch/Case equvilent
a  = 20

if a < 5:
    print("1")
elif a < 10:
    print("2")
elif a < 20:
    print("3")
else:
    print("4")


# Ternary Operator
a = 25
if a < 5:
    b = 'a < 5'
else:
    b = 'b >= 5'

print("B is :", b)

b = 'a < 5' if a < 5 else 'a >= 5'
print(b)
