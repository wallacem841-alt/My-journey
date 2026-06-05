thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # to copy a list you have to do this otherwise you will just link the 2 lists
# you can also use (mylist = list(thislist))
#print(mylist)

foods = ["apple", "banana", "cherry"]
o_p_originals = ['joui', 'Kaiser', 'Arthur']
z = foods + o_p_originals # this merges both list as they are.

r = o_p_originals # this links both lists.

'''
for _ in foods:
    o_p_originals.append(_)
'''
# z = foods + o_p_originals # if after the function this prints foods twice

o_p_originals.append('Dante')

print(z)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2) # this extends list1 with the itens from list2
print(list1) # this prints ['a', 'b', 'c', 1, 2, 3]


list3 = list1 * 2

print(list3) # this prints ['a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c', 1, 2, 3]

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

'''
1. index()
The index() method is used to find the first occurrence of a specific element in a list. If the element is found,
it returns the index (position) of the element. If the element isn't found, Python will raise a ValueError.

Here's the basic syntax for index():

list.index(element, start, end)

element: This is the item you are searching for in the list.
start (optional): The starting index from where the search should begin.
end (optional): The ending index where the search should end.

Example:

fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'banana']
print(fruits.index('banana'))  # Output: 1
print(fruits.index('banana', 2))  # Output: 5 (search starts from index 2)
If you try to find an element that isn't in the list, it will throw an error:

print(fruits.index('orange'))  # Raises ValueError
'''

'''
2. sort()
The sort() method is used to sort the elements of a list in ascending or descending order. It modifies the list in place, which means it changes the original list.

Here's how you use sort():

list.sort(key=None, reverse=False)

key (optional): A function that serves as a key for the sort comparison.
reverse (optional): A Boolean value. If set to True, the list elements are sorted as if each comparison were reversed (descending order).
Example:

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
To sort using a custom key:

fruits = ['banana', 'apple', 'fig', 'cherry']
fruits.sort(key=len)  # Sort by the length of each element
print(fruits)  # Output: ['fig', 'apple', 'banana', 'cherry']
In this way, index() helps you find elements, while sort() helps you order them. Both are incredibly useful for managing lists in Python!
'''