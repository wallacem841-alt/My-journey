# To add one item to a set use the add() method.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) # {'cherry', 'orange', 'banana', 'apple'}

# To add items from another set into the current set, use the update() method.

tropical = {"pineapple", "mango", "papaya"} 

thisset.update(tropical)

print(thisset) # {'cherry', 'orange', 'apple', 'mango', 'papaya', 'banana', 'pineapple'}

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).


#To remove an item in a set, use the remove(), or the discard() method.

thisset.remove("banana") # Note: If the item to remove does not exist, remove() will raise an error. (KeyError: "x")

print(thisset) # {'cherry', 'orange', 'apple', 'mango', 'papaya', 'pineapple'}

# Remove "banana" by using the discard() method:

thisset.discard("banana") # Note: If the item to remove does not exist, discard() will NOT raise an error.S

print(thisset) # {'cherry', 'mango', 'papaya', 'apple', 'orange', 'pineapple'}

# You can also use the pop() method to remove an item, but this method will remove a random item,
# so you cannot be sure what item that gets removed.

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:

thisset.clear()

print(thisset) # set()

# The del keyword will delete the set completely:

del thisset

# print(thisset) # NameError: name 'thisset' is not defined