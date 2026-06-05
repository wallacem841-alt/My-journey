
user_input = input('Give me a text: ')

character_times = []

for x in range(len(user_input)):
    number_times = 0

    for y in range(len(user_input)):
        if user_input[y] == user_input[x]:
            number_times += 1
    
    character_times.append(number_times)

for x in range(len(character_times)):
    if character_times[x] == 1:
        print('The fist unique character is : ' + user_input[x])
        break
    elif x == len(character_times) - 1:
        print('No unique character found')