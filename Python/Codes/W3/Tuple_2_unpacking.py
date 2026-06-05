fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

'''
Result:
apple
banana
cherry
'''

# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

'''
Result:
apple
banana
['cherry', 'strawberry', 'raspberry']
'''

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.

'''
Result:
apple
['mango', 'papaya', 'pineapple']
cherry
'''