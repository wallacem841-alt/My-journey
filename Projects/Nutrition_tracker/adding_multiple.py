import sqlite3
from datetime import datetime

def is_valid_date_string(date_string, date_format="%d/%m/%Y"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False
    
def add_meal(meal_date, meal_type, list_of_foods):

    if not is_valid_date_string(meal_date):
        return "invalid_date"
    
    for i in list_of_foods:
        try:
            i["weight"] = float(i["weight"])

        except ValueError:
            return "string_as_weight"
        
    conn = sqlite3.connect('nutrition_tracker.db')
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute('PRAGMA foreign_keys = ON;')

    foods_not_in_db = []

    for i in list_of_foods:
        # Fetch food data from food_db for the given food_name
        cursor.execute('SELECT weight, protein, carbs, fat, kalories FROM food_db WHERE name = ?', (i["name"],))
        food_data = cursor.fetchone()

        if food_data:
            # Extract food data
            base_weight, base_protein, base_carbs, base_fat, base_kalories = food_data
            
            # Calculate the nutritional values based on the input weight
            protein = (base_protein / base_weight) * i["weight"]
            carbs = (base_carbs / base_weight) * i["weight"]
            fat = (base_fat / base_weight) * i["weight"]
            kalories = (base_kalories / base_weight) * i["weight"]

            try:
                # Insert the meal into meals_db
                cursor.execute('''INSERT INTO meals_db (date, meal, food, weight, protein, carbs, fat, kalories) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                            (meal_date, meal_type, i["name"], i["weight"], protein, carbs, fat, kalories))
                conn.commit()
            except sqlite3.DatabaseError:
                conn.close()
                return 'DatabaseError'
        
        else:
            foods_not_in_db.append(i["name"])

    conn.close()

    return foods_not_in_db


# Example usage

list_test = [
    {"name": "Rice", "weight": 200},
    {"name": "Bread", "weight": 50},
    {"name": "not_in_db_test", "weight": 50}
]

test = add_meal('21/12/2024', 'dinner', list_test)

print(test)