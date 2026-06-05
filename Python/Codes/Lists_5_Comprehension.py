fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" not in x] #this is equal to:
'''
for x in fruits:
    if "a" not in x:
        newlist.append(x)
'''

'''The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.'''

newlist2 = [x if x != "banana" else "orange" for x in fruits]

newlist3 = [x for x in fruits if "apple" in x]

print(newlist)
print(newlist2)
print(newlist3)

tuple_from_gen = tuple(x for x in range(5)) # this approach is more memory efficient but slower

print(tuple_from_gen)