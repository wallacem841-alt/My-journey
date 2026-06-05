'''
import random

random_encounters = []

R = []

for _ in range(20):
    Ra = random.randint(0, len(random_encounters) - 1) # This line generates a random integer Ra in the range from 0 to the length of random_encounters minus 1. It's essentially picking a random index within the current range of the random_encounters list.
    Ri = random_encounters[Ra] # This line selects the element at index Ra from the random_encounters list and assigns it to Ri.
    random_encounters.pop(Ra) # This line removes the element at index Ra from the random_encounters list.
    R.append(Ri) # This line appends the randomly selected element Ri to the R list.
'''

# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # to sort the other way around = thislist.sort(reverse = True)
print(thislist)

# Sort the list numerically:

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort() # to simply reverse the list = thislist.reverse()
print(thislist1)

# Perform a case-insensitive sort of the list:

thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key=str.lower)
print(thislist2)
# if not done like this it will sort the upper case first

def myfunc(n):
  return abs(n - 50)

thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(key = myfunc)
print(thislist4)

'''
def myfunc(n):: This line defines a function named myfunc that takes one parameter n.
This function calculates the absolute difference between n and the number 50.

return abs(n - 50): Inside the function myfunc, abs(n - 50) calculates the absolute value of the difference between the argument n
and the number 50. This function essentially measures how far n is from 50 regardless of whether n is greater or smaller than 50.

In this case, the sorting happens based on the absolute differences of each element from 50:

abs(100 - 50) = 50
abs(50 - 50) = 0
abs(65 - 50) = 15
abs(82 - 50) = 32
abs(23 - 50) = 27

So, the sorted list becomes [50, 65, 23, 82, 100].
'''

