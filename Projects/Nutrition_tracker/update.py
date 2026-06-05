import sqlite3

def update_foods(columns, values, food_id):
    if len(columns) != len(values):
        return "Columns_values_mismatch"

    # Build the SET part of the query dynamically
    set_clause = ", ".join([f"{col} = ?" for col in columns])

    # Construct the SQL query
    query = f"UPDATE food_db SET {set_clause} WHERE name = ?"

    conn = sqlite3.connect('nutrition_tracker.db')
    cursor = conn.cursor()

    try:
        # Execute the query with values + food_id
        cursor.execute(query, values + [food_id])
    except sqlite3.DatabaseError:
        conn.close()
        return "DatabaseError"
    except sqlite3.IntegrityError:
        conn.close()
        return "Name_exists_in_db"
    
    if cursor.rowcount == 0:
        conn.close()
        return "Item_not_in_db"

    conn.commit()
    conn.close()

    return 0

#Example usage. note to self. make sure values are floats except name in GUI
#note 2 the lists can be any size but they have to match

'''columns = ['name', 'weight', 'protein', 'carbs', 'fat', 'kalories']

values = ['Orange', 100, 0.9, 12, 0.1, 47]

test = update_foods(columns, values, "orange")

print(test)'''