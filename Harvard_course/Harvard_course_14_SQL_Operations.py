import sqlite3
import sys

class Action:

    def adding(self):
        adding = [input("Give me a waifu: ")]

        connection = sqlite3.connect('adress.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM adress WHERE name = ?', adding)
        result = cursor.fetchone()

        if result:
            print(f"'{adding}' is already in the database!")
        else:
            # If not, insert the new entry
            cursor.execute('INSERT INTO adress (name) VALUES (?)', adding)
            connection.commit()
            print("Waifu added successfully!")
        
        connection.close()

    def assign(self):
        adding = input("Give me a waifu: ")

        try:
            house = int(input("Where does she lives? "))
        except ValueError:
            print("House must be a integer")
            return
        
        connection = sqlite3.connect('adress.db')
        cursor = connection.cursor()

        # Combine checks into one query to optimize database interaction
        cursor.execute('SELECT * FROM adress WHERE name = ? OR adress = ?', (adding, house))
        result = cursor.fetchone()

        if result:
            if result[1] == adding:
                print(f"'{adding}' is already in the database!")
            elif result[0] == house:
                print(f"House '{house}' is already occupied!")
        else:
            # If not, insert the new entry
            cursor.execute('INSERT INTO adress (adress, name) VALUES (?, ?)', (house, adding))
            connection.commit()
            print("Waifu added successfully!")
        connection.close()

    def exclude(self):
        question = input("Exclude by 'adress' or 'waifu'? ").lower()
        if question == 'waifu':
            excluding = input('Which waifu is going away? :( ')

            connection = sqlite3.connect('adress.db')
            cursor = connection.cursor()

            cursor.execute("DELETE FROM adress WHERE name = ?", (excluding,))
            connection.commit()

            if cursor.rowcount > 0:
                print(f"{excluding} successfully deleted! Hopefully she'll be back soon")
            else:
                print(f"No waifu found with the name '{excluding}' to delete.")
            connection.close()
            
        elif question == 'adress':
            try:
                excluding = int(input("Which house you're vacating? "))
            except ValueError:
                print("House must be a integer")
                return

            connection = sqlite3.connect('adress.db')
            cursor = connection.cursor()

            cursor.execute('SELECT name FROM adress WHERE adress = ?',(excluding,))
            result = cursor.fetchone()

            if result:
                # Delete the record if a match was found
                cursor.execute("DELETE FROM adress WHERE adress = ?", (excluding,))
                connection.commit()

                if cursor.rowcount > 0:
                    print(f"House {excluding} successfully vacated. {result[0]} was in that house.")
                else:
                    print(f"An error occurred while trying to vacate house {excluding}.")
            else:
                print(f"The house {excluding} isn't in the registry yet.")
            connection.close()

        else:
            print("Not a valid input")

    def list(self):
        connection = sqlite3.connect('adress.db')
        cursor = connection.cursor()

        cursor.execute('SELECT name, adress FROM adress')
        result = cursor.fetchall()
        connection.close()
        for row in result:
            print(f"{row[0]} lives in house {row[1]}")

    def update(self):
        updating_waifu = input('Which waifu is moving? ')
        
        try:
            updating_house = int(input('To were? '))
        except ValueError:
            print('House must be an integer!')
            return

        connection = sqlite3.connect('adress.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE adress SET adress = ? WHERE name = ?", (updating_house, updating_waifu))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"{updating_waifu} successfully moved!")
        else:
            print(f"No waifu found with the name '{updating_waifu}' to move.")
        connection.close()

    def execute_action(self, action_name):
        # Get the method name dynamically and check if it exists
        method = getattr(self, action_name, None)
        if method:
            # Directly call the method based on user input
            getattr(self, action_name)()
        else:
            print("Not a valid function")

# Main program
action = Action()

while True:

    user_input = input("What do you want to do? or press E to exit: ")

    if user_input.upper() == "E":
        break
    else:
        # Call the method based on user input
        action.execute_action(user_input)

sys.exit(0)