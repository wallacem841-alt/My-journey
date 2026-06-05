user_input = input('Give me a text: ')

character_count = {}

for char in user_input:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1

empty_value = character_count.pop(' ', 0)

sorted_by_key = dict(sorted(character_count.items()))

sorted_by_value = dict(sorted(character_count.items(), key=lambda item: item[1]))

print('Sorted alphabetically')
print(sorted_by_key)

print('Sorted by value')
print(sorted_by_value)

print(f'There are {empty_value} spaces')