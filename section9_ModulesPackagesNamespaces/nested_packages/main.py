
import section9_ModulesPackagesNamespaces.nested_packages.common.validators as validators
import section9_ModulesPackagesNamespaces.nested_packages.common

print("\n\n**** self *****")
# Will fail because k needs to be added to the globals namespace
# The globals dic is modified while we run trhough it. Runtime error
#         for k in globals().keys():
#             print(k)

for k in dict(globals()).keys():
    print("\t", k)


print("\n\n***** common *****")
for k in common.__dict__.keys():
    print("\t", k)

# Validators has the modules in it's namespace
print("\n\n***** validators *****")
for k in common.validators.__dict__.keys():
    print("\t", k)


# boolean has the boolean functions in it's namespace
print("\n\n***** boolean *****")
for k in common.validators.boolean.__dict__.keys():
    print("\t", k)