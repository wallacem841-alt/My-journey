thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

'''
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
'''

for x in thisdict:
  print(x) # brand model year

# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x]) # Ford Mustang 1964

# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x) # Ford Mustang 1964

# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x) # brand model year

# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y) # brand Ford model Mustang year 1964

'''You cannot copy a dictionary simply by typing dict2 = dict1,
because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
'''

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Another way to make a copy is to use the built-in function dict().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}