# Access Items
# You cannot access items in a set by referring to an index or a key.

# Loop

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# this prints the items randomly

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) # this prints True

print("banana" not in thisset) # this prints False

'''
The frozenset is an immutable version of a regular set in Python. Because it is immutable,
its contents cannot be modified after it is created. This makes it useful in situations where you need a set that will not change over time,
such as using it as a key in a dictionary or as an element in another set.
'''

# You can create a frozenset from any iterable (like lists, tuples, strings, or other sets).

# Create a frozenset from a list
fs1 = frozenset([1, 2, 3, 4, 5])

# Create a frozenset from a tuple
fs2 = frozenset((2, 3, 4))

# Create a frozenset from a string
fs3 = frozenset("hello")

for x in fs1:
  print(x)