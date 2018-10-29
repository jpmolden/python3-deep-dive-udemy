

def pprint_dict(header, d):
    print("\n\n-----------------------")
    print("****** {0} ******".format(header))
    for key, value in d.items():
        print(key, value)
    print("-----------------------\n\n")
