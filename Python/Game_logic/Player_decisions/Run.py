import json
import sys

player_classes = ["knight", "sorcerer", "bandit"]

name = input("welcome player what's your name: ")

while True:
    try:
        age = int(input("how old are you? "))
        if age >= 16:
            break
        else:
            print("You're to young to play this game :(")
            sys.exit()

    except ValueError:
        print("Please enter a number!")

while True:
    player_class = input(f"do you want to play as a {player_classes}? ")
    if player_class.lower() in player_classes:
        print(f"Confirmed {player_class}!")
        break
    else:
        print("Select one of the classes")

with open("Starter_inventory.json", "r") as f:
    data = json.load(f)  # load the JSON data into a Python dict
    starter_inventory = data[player_class.lower()]

player_data = {"player": {
    "name": name,
    "age": age,
    "class": player_class.lower(),
    "level": 1,
    "inventory": starter_inventory
}}

with open("savefile.json", "w") as f:
    json.dump(player_data, f, indent=4)

with open("savefile.json", "r") as f:
    player_data = json.load(f)

#Game start:
print(f"Welcome to the {player_data["player"]["class"]} named {player_data["player"]["name"]}!")
print(f"You may eat as much as you like!")

with open("Possible_choices.json", "r") as f:
    data = json.load(f)
    scene_1_eating_choices = data["scene_1_eating"]

while True:
    eat_choice = input(f"In front of you there is {scene_1_eating_choices}, pick one: ").lower()
    if eat_choice in scene_1_eating_choices:
        print(f"you ate {eat_choice}!")
        break
    else:
        print("The table doesn't have that")

with open("Player_choices.json", "r") as f:
    data = json.load(f)

data["scene_1_eating"] = eat_choice

with open("Player_choices.json", "w") as f:
    json.dump(data, f, indent=4)

with open("Possible_choices.json", "r") as f:
    data = json.load(f)
    scene_1_greating_choices = data["scene_1_greating"]

while True:
    greating_choice = input(f"The king enters the room what do you do? {scene_1_greating_choices}: ").lower()
    if greating_choice in scene_1_greating_choices:
        break
    else:
        print("That is not an option")

with open("Player_choices.json", "r") as f:
    data = json.load(f)

data["scene_1_greating"] = greating_choice

with open("Player_choices.json", "w") as f:
    json.dump(data, f, indent=4)

with open("Player_choices.json", "r") as f:
    data = json.load(f)
with open("savefile.json", "r") as f:
    player_data = json.load(f)
if data["scene_1_greating"] == "peace sign":
    print(f"The king has cut {player_data["player"]["name"]}'s head.")
    print(f"The player has lived until {player_data["player"]["age"]} years old.")