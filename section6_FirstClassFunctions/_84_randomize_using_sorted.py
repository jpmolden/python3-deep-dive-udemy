# Using sorted to make a random sort

from random import random

l = [1,2,3,4,5,6,7]

print(sorted(l, key=lambda e: random()))

l = {'a': 1,
     'b': 2,
     'c': 3,
     'd': 4,
     'e': 5,
     'f': 6,
     'g': 7,
     }

print(sorted(l, key=lambda e: random()))