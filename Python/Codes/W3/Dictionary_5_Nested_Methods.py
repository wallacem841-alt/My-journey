# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

'''
Or, if you want to add three dictionaries into a new dictionary:

Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
'''

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

print(myfamily["child2"]["name"]) # Tobias

# You can loop through a dictionary by using the items() method like this:

for x, obj in myfamily.items(): # n each iteration, x will represent the key ("child1", "child2", "child3"),
  # and obj will represent the corresponding dictionary (e.g., child1, child2, child3).
  print(x)

  for y in obj:
    print(y + ':', obj[y])
'''
Inside the loop, another loop iterates over the dictionary obj. Since obj represents a dictionary,
iterating over it directly will give you its keys. So, in each iteration of the inner loop, y will represent a key in the dictionary
obj (e.g., "name", "year"), and obj[y] will give you the corresponding value.
'''

# print

'''
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011
'''

# Python has a set of built-in methods that you can use on dictionaries.

'''
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''