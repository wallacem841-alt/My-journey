words = ["apple", "banana", "cherry", "date"]

for word in words: # use the for loop to print out items in the list
    capitalized_word = word.capitalize() # you can make operations with them
    print(f"The capitalized form of {word} is {capitalized_word}")

numbers = [2, 4, 6, 8, 10]

for num in numbers:
    square = num ** 2
    print(f"The square of {num} is {square}")

'''
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): # this is another way to loop a list. GPT says is less preferable for readability reasons
  print(thislist[i])
'''

'''
#this is a bit more complicaded
thislist = ["apple", "banana", "cherry"] #this is the list
i = 0 # this is the index
while i < len(thislist): #This activates an operation that is happening until i is Smaller than len(thislist)
# at this point i = 0 and len(thislist) = 3
  print(thislist[i]) #this prints out one list element indicaded by the index i witch is 0
  i = i + 1 # this ads 1 to the index. So next time the opperation occurs it will print out banana insted of apple.
'''