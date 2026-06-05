'''
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) 
# You can use the | operator instead of the union() method, and you will get the same result.
# set3 = set1 | set2
print(set3) # {1, 2, 3, 'b', 'c', 'a'}

set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 |set4
print(myset)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# The update() method inserts the items in set2 into set1:

set1.update(set2)
print(set1) # {1, 2, 3, 'c', 'a', 'b'}

# Note: Both union() and update() will exclude any duplicate items.

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
# You can use the & operator instead of the intersection() method, and you will get the same result.
# set3 = set1 & set2
print(set3) # {'apple'}

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersecton() method.

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1) # {'apple'}

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) 
# You can use the - operator instead of the difference() method, and you will get the same result.
# set3 = set1 - set2
print(set3) # {'banana', 'cherry'}

# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# The difference_update() method will also keep the items from the first set that are not in the other set,
# but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) # {'banana', 'cherry'}

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# set3 = set1 ^ set2
print(set3) # {'banana', 'google', 'microsoft', 'cherry'}

# Note: The ^ operator only allows you to join sets with sets,
# and not with other data types like you can with the symmetric_difference() method.

# The symmetric_difference_update() method will also keep all but the duplicates,
# but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) # {'google', 'microsoft', 'cherry', 'banana'}

'''
Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
'''