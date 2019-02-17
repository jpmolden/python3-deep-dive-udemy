print('\n*** Tuples, Lists and Strings are sequence types **')


print('\tTuples')
# Containers
# Order matters
# Either Heterogeneous or Homogeneous
# Indexable
# Iterable

# Immutable
#     Fixed length
#     Fixed order
#         No in place sorts
#         No in place reversals



print('\tLists')
# Containers
# Order matters
# Either Heterogeneous or Homogeneous
# Indexable
# Iterable

# Mutable
#     Variable length
#     Variable order
#         Can do place sorts
#         Can do place reversal



print('\tStrings')
# Containers of characters
# Order matters
# Homogeneous
# Indexable
# Iterable

# Immutable
#     Fixed length
#     Fixed order
#         No in place sorts
#         No in place reversals

# Tuple as a data structure
# Point  (10, 20)  x, y coordinates
# Circle (0,0,10)  x, y, radius

# City ("London", "UK", 8_780_000) City, Country, Population
# print(10_500_750)
london   = ("London",   "UK",  8_780_000)
new_york = ("New York", "UK",  8_500_000)
beijing  = ("Beijing",  "UK", 21_000_000)
cities = [london, new_york, beijing]

print('\n*** Extracting data from tuples **')
print(cities)
total_pop = 0
for city in cities:
    total_pop += city[2]

print("Total population =", total_pop)

print('\n*** Unpacking **')
# The , is what creates a tuple not the ( )
# Packing
manchester = "Manchester", "UK", 2_000_000
city, country, population = manchester
print(manchester)

print('\n*** Dummy Variables **')
city, _, _ = london
print(city)
print(_)

print('\n*** Extended unpacking **')
# symbol, year, month, day, open, high, low, close
record = ("DJIA", 2018, 1, 19, 25978.50, 27000.54, 24000.30, 26701.22)
# The bad way!!!
# symbol, year, close = record[0], record[1], record[7]
symbol, year, month, day, *_, close = record


