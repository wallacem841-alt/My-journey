import random

V1 = "Spider"
V2 = "Heath potion"
V3 = "Rusty dagger"
V4 = "Spoiled apple"
V5 = "empty"

Random_encounter = [V1,V2,V3,V4,V5,V5,V5,V5,V5,V5]

list_len = len(Random_encounter)

R1a = random.randint(0, len(Random_encounter) - 1)
R1 = Random_encounter[R1a]
Random_encounter.pop(R1a)

R2a = random.randint(0, len(Random_encounter) - 1)
R2 = Random_encounter[R2a]
Random_encounter.pop(R2a)

R3a = random.randint(0, len(Random_encounter) - 1)
R3 = Random_encounter[R3a]
Random_encounter.pop(R3a)

R4a = random.randint(0, len(Random_encounter) - 1)
R4 = Random_encounter[R4a]
Random_encounter.pop(R4a)

R5a = random.randint(0, len(Random_encounter) - 1)
R5 = Random_encounter[R5a]
Random_encounter.pop(R5a)

R6a = random.randint(0, len(Random_encounter) - 1)
R6 = Random_encounter[R6a]
Random_encounter.pop(R6a)

R7a = random.randint(0, len(Random_encounter) - 1)
R7 = Random_encounter[R7a]
Random_encounter.pop(R7a)

R8a = random.randint(0, len(Random_encounter) - 1)
R8 = Random_encounter[R8a]
Random_encounter.pop(R8a)

R9a = random.randint(0, len(Random_encounter) - 1)
R9 = Random_encounter[R9a]
Random_encounter.pop(R9a)

R10a = random.randint(0, len(Random_encounter) - 1)
R10 = Random_encounter[R10a]
Random_encounter.pop(R10a)

idx = 0

while idx < list_len:
    imp = eval(input("Good luck player: "))
    print(imp)
    idx = idx + 1

input('Press enter to exit...')

''' for version 2.0
import random

random_encounters = []

R = []

for _ in range(20):
    Ra = random.randint(0, len(random_encounters) - 1) # This line generates a random integer Ra in the range from 0 to the length of random_encounters minus 1. It's essentially picking a random index within the current range of the random_encounters list.
    Ri = random_encounters[Ra] # This line selects the element at index Ra from the random_encounters list and assigns it to Ri.
    random_encounters.pop(Ra) # This line removes the element at index Ra from the random_encounters list.
    R.append(Ri) # This line appends the randomly selected element Ri to the R list.
'''
'''import random

my_list = [1, 2, 3, 4, 5]

# Shuffle the list in-place
random.shuffle(my_list)

print(my_list)'''