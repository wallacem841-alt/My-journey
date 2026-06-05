thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets # this makes a tuple
print(thistuple)

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''

'''
Immutability: Tuples are immutable, meaning once they are created, their elements cannot be changed or modified.
This immutability provides a level of safety when passing around data that should not be altered accidentally.

Performance: Tuples are generally more memory efficient and faster than lists because they are immutable.
This means that Python does not need to allocate extra space or time to handle potential modifications to the data structure.

Sequence Unpacking: Tuples support sequence unpacking,
allowing you to easily assign multiple variables in a single line using a tuple on the right-hand side of the assignment.

Hashability: Tuples are hashable if all their elements are hashable.
This means tuples can be used as keys in dictionaries and as elements of sets, while lists cannot,
because lists are mutable and their hash value can change if their contents are modified.

Use as Dictionary Keys: Because of their immutability and hashability,
tuples can be used as keys in dictionaries when the keys need to represent fixed combinations of values.
'''