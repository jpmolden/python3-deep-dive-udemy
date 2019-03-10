
# Writing an api.py

# Better - bu unweildy (too may imports)
#
# api/
#     api.py
#     dbutilies.py
#         connections.py
#         queries.py
#     jsonutilities.py
#     typeconversion.py
#     authentication.py
#     authorization.py
#     users.py
#     loggin.py


# Better
#
# api/
#     utilities/
#         __init__.py
#         databases/
#             __init__.py
#             connections.py
#             queries.py
#         json/
#             __init__.py
#             encoders.py
#             decoders.py
#     security/
#         __init__.py
#         authorization.py
#         authentication.py
#     models/
#         __init__.py
#         users/
#             __init__.py
#             user.py
#             userprofiles.py



# Module developers perspective
# mylib/
#     __init__.py
#     submod1.py
#     submod2.py
#     subpack1/
#         __init__,py
#         pack1mod1.py
#         pack1mnd2.py

#     For a user
#     import mylib
#     mylib.myfunc(), mylib.MyClass()



# Using __init__.py
#     Expose just whats need by users
    #mylib.__init__.py
        # from mylib.submod1 import myfunc
        # from mylib.submod1.pack1mod2 import MyClass

#     This hides the internal implementation









