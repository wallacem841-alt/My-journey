import sqlite3
import csv

def food_register(name, weight, protein, carbs, fat, kalories):
    # Connect to the database
    conn = sqlite3.connect('nutrition_tracker.db')
    cursor = conn.cursor()

    
    try:
        cursor.execute('''INSERT INTO food_db (name, weight, protein, carbs, fat, kalories)
                        VALUES (?, ?, ?, ?, ?, ?)''', (name, weight, protein, carbs, fat, kalories))
        conn.commit()
    except sqlite3.IntegrityError:
        # Close the connection
        conn.close()
        return 'IntegrityError'
    except sqlite3.DatabaseError:
        conn.close()
        return 'DatabaseError'
    
    conn.close()
    return 0

result = food_register("orange", 150, 0.5, 25, 0.3, 95)
print(result) #example input

def csv_food_register(path, name, weight, protein, carbs, fat, kalories):
    conn = sqlite3.connect('nutrition_tracker.db')
    cursor = conn.cursor()

    csv_food_register_errors = []

    with open(path, 'r') as file:
        csv_reader = csv.DictReader(file)

        required_columns = {name, weight, protein, carbs, fat, kalories}
        if not required_columns.issubset(set(csv_reader.fieldnames)):
            conn.close()
            return csv_food_register_errors, 'MissingColumnsError'
        
        for row in csv_reader:

            try:
                row_name = str(row[name])
                row_weight = float(row[weight])
                row_protein = float(row[protein])
                row_carbs = float(row[carbs])
                row_fat = float(row[fat])
                row_kalories = float(row[kalories])
            except ValueError:
                csv_food_register_errors.append(row[name])  # Log the row causing the issue
                continue  # Skip to the next row



            try:
                cursor.execute('''INSERT INTO food_db (name, weight, protein, carbs, fat, kalories)
                                VALUES (?, ?, ?, ?, ?, ?)''', (row_name, row_weight, row_protein,
                                row_carbs, row_fat, row_kalories))
            except sqlite3.IntegrityError:
                # Close the connection
                csv_food_register_errors.append(row_name)
            except sqlite3.DatabaseError:
                #Commit the changes and close the connection
                conn.commit()
                conn.close()
                return csv_food_register_errors, 'DatabaseError'
        
        #Commit the changes and close the connection
        conn.commit()
        conn.close()

    return csv_food_register_errors, 0

#'''path = r"C:\Users\Usuario\Desktop\Novo(a) Planilha OpenDocument.csv"

'''repeted, status = csv_food_register(path, "Food","serving_size","protein","carbs","fat","calories")

for i in repeted:
    print(i)

print(status)''' #example input