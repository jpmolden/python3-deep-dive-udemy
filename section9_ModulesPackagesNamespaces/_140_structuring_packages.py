
import section9_ModulesPackagesNamespaces.shared as shared
# import shared.validators.json
# import shared.validators.date
# import shared.validators.boolean
# import shared.validators.numeric



print("\n\n**** self *****")
# Will fail because k needs to be added to the globals namespace
# The globals dic is modified while we run trhough it. Runtime error
#         for k in globals().keys():
#             print(k)

for k in dict(globals()).keys():
    print("\t", k)


print("\n\n***** shared *****")
for k in shared.__dict__.keys():
    print("\t", k)

# Validators has the modules in it's namespace
print("\n\n***** validators *****")
for k in shared.validators.__dict__.keys():
    print("\t", k)


# boolean has the boolean functions in it's namespace
print("\n\n***** boolean *****")
for k in shared.validators.boolean.__dict__.keys():
    print("\t", k)


# Reducing the tedious imports
# Adding the * import to the __init__ makes a shared api type interface
# Like this
# Even though the shared namespace did not include the boolean_helper initially
# shared.bolean_helper






