# Print the name of the module that's running
print(f"Running: {__name__}")

def pprint_dict(header, d):
    print('\n--------------------------------------')
    print(f'***** pprint_dict of {header} *****')
    for k, v in d.items():
        print("\t", k, v)
    print('--------------------------------------\n')


# Print the dict of the current scope's global variables
pprint_dict('module1.globals', globals())
print(f'{"*" * 10} End of {__name__} {"*" * 10}')
# Modules have an execution space any they execute


