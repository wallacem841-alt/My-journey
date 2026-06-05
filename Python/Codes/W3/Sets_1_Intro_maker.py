# Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

'''
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
'''

thisset = {"apple", "banana", "cherry", "apple"} 

print(thisset) # this prints {'apple', 'cherry', 'banana'}

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0} # it erases the 2nd value

print(thisset) # this prints {False, True, 2, 'banana', 'apple', 'cherry'}

# It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) # this prints {'cherry', 'banana', 'apple'}

'''
Uniqueness: Sets contain only unique elements. When you add duplicate elements to a set,
only one instance of each unique element is retained. This property is useful for eliminating duplicate entries from a collection of data.

Fast Membership Testing: Sets offer constant-time average complexity for membership testing (i.e., checking if an element is present in the set), 
which makes them highly efficient for large datasets.
This is especially beneficial when dealing with large collections of data where quick lookups are necessary.

Mathematical Set Operations: Sets in Python support various mathematical set operations such as union, intersection, difference,
and symmetric difference. These operations allow you to perform common set operations easily and efficiently.

Mutability and Immutability: Python provides both mutable (set) and immutable (frozenset) set types.
While sets allow modification (adding and removing elements),
frozensets are immutable and can be used as keys in dictionaries or elements in other sets.

Iterability: Sets are iterable, meaning you can iterate over the elements in a set using a loop or other iterable methods.
This feature makes sets convenient for tasks where you need to iterate over unique elements without duplicates.

Efficient Storage and Retrieval: Internally, sets are implemented using hash tables, which provide efficient storage and retrieval of elements.
This implementation ensures that sets maintain their high performance characteristics even with large numbers of elements.
'''