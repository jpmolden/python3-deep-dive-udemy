
print('*** Using python >=3.5 ***')

l = [1, 2, 3, 4, 5, 6]

# Unpacking using slicing, :
a, b = l[0], l[1:]

print('\n**** Using the * Operator ***')

print('\ta, *b = l')
a, *b = l
print("\ta={}\n\tb={}".format(a,b))

print('\tThis works with any iterable including non-sequence types (set, dict)')
c, *d = (1,2,3,4,5)
print('\tWe always unpack with * into a list')
print("\tc={}\n\td={}".format(c,d))

print('\n*** Will pick up the rest if an iterable ***')
a, b, *c, d = [1,2,3,4,5,6,7,8,9,10]
print("\ta={}\n\tb={}\n\tc={}\n\td={} (Last)".format(a,b,c,d))
a, b, *c, d = "WXYYYZ"
print("\n\ta={}\n\tb={}\n\tc={}\n\td={} (Last)".format(a,b,c,d))


print('\n*** Can use on the RHS ***')
l1 = [1,2,3]
l2 = [4,5,6]
l = [*l1, *l2]
print('\tCombined list')
print("\t{}".format(l))

print('\n*** * Works on any iterable ***')
print('\tUnpacking into a set\list')
d1 = {'a': 1,
      'B': 2,
      'C': 34,
      'd': 3
      }

d3 = {'F': 1,
      'S': 2,
      'a': 34,
      'd': 3
      }

d2 = {'b': 1,
      'L': 2,
      'z': 34,
      'a': 3
      }

s = {*d1, *d2, *d3}
print("\t", s)

l = [*d1, *d2, *d3]
print("\t", l)

print('\n*** ** Operator (Dictionary key value merge ***')
print('\td3 Takes precidence!!!!')
print('\tMerging dictionaries')
d4 = {**d1, **d2, **d3}
print("\t", d4)


print('\n*** Nested Unpacking ***')
l = [1, 2, [3,4]]
a, b, (c, d) = l
print("\ta={}\n\tb={}\n\tc={}\n\td={} (Last)".format(a,b,c,d))


print('\n\tNested unpacking with *')
a, *b, (c, *d) = [1,2,3,'python']
print("\ta={}\n\tb={}\n\tc={}\n\td={} (Last)".format(a,b,c,d))


print('\n*** Set union unpacking')
s1 = {1,2,3}
s2 = {1,2,4}
s3 = {1,2,5}
s4 = {1,2,6}

# Unpacking into set
set5 = {*s1, *s2, *s3, *s4}
print("\t", set5)


# Unpacking into list
list5 = {*s1, *s2, *s3, *s4}
print("\t", list5)






