import sqlite3

import sqlite3

# Step 1: Connect to a database (or create one if it doesn't exist)
connection = sqlite3.connect('adress.db')

# Step 2: Create a cursor object
cursor = connection.cursor()

# Step 3: Create a table using SQL command
cursor.execute('''
CREATE TABLE IF NOT EXISTS adress (
    adress INTEGER PRIMARY KEY,     -- Unique adress for each wifu
    name TEXT NOT NULL   -- wifu's name
)
''')

# Step 4: Commit the changes
connection.commit()

# Step 5: Close the connection
connection.close()

print("Table 'adress' created successfully.")
