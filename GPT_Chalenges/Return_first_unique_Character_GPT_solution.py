# Step 1: Count the frequency of each character
user_input = input('Give me a text: ')
character_count = {}

for char in user_input:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1

# Step 2: Find the first character with a count of 1
for char in user_input:
    if character_count[char] == 1:
        print('The first unique character is:', char)
        break
else:
    print('No unique character found')