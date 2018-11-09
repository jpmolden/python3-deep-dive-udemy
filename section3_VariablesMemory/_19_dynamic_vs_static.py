

print(" *** Variables are reference to an object ***")
myvar = "hello"
print("\tVariables are reference to an object: ", type(myvar))
myvar = 10
print("\tVariables are reference to an object: ", type(myvar))


a = lambda x: x**2

print("a(2) = ", a(2))
print("\ta is type: ", type(a))


# Variable reassignment changes the mem addr of the reference not the memory contents
print(hex(id(myvar)))
myvar = "ssmdf"
print(hex(id(myvar)))
myvar = print
print(hex(id(myvar)))
myvar = 10
print(hex(id(myvar)))
myvar = myvar + 10
print(hex(id(myvar)))
myvar = myvar + 10
print(hex(id(myvar)))

# The value inside of in object can NEVER be changed, instead a new int object is created