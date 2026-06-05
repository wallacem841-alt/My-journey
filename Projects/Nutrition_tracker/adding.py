import sqlite3
from datetime import datetime

def is_valid_date_string(date_string, date_format="%d/%m/%Y"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def add_meal(meal_date, meal_type, food_name, weight):

    if not is_valid_date_string(meal_date):
        return "invalid_date"
    
    try:
        weight = float(weight)
    
    except ValueError:
        return "string_as_weight"

    conn = sqlite3.connect('nutrition_tracker.db')
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute('PRAGMA foreign_keys = ON;')

    # Fetch food data from food_db for the given food_name
    cursor.execute('SELECT weight, protein, carbs, fat, kalories FROM food_db WHERE name = ?', (food_name,))
    food_data = cursor.fetchone()

    if food_data:
        # Extract food data
        base_weight, base_protein, base_carbs, base_fat, base_kalories = food_data
        
        # Calculate the nutritional values based on the input weight
        protein = (base_protein / base_weight) * weight
        carbs = (base_carbs / base_weight) * weight
        fat = (base_fat / base_weight) * weight
        kalories = (base_kalories / base_weight) * weight

        try:
            # Insert the meal into meals_db
            cursor.execute('''INSERT INTO meals_db (date, meal, food, weight, protein, carbs, fat, kalories) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                        (meal_date, meal_type, food_name, weight, protein, carbs, fat, kalories))
            conn.commit()
        except sqlite3.DatabaseError:
            conn.close()
            return 'DatabaseError'
        
    else:
        conn.close()
        return "food_not_in_db"

    conn.close()

    return 0

# Example usage
test = add_meal('03/12/2024', 'dinner', 'Rice', 200)

print(test)
