import sqlite3
import csv

# Step 1: Connect to the database
connection = sqlite3.connect('adress.db')
cursor = connection.cursor()

# Step 2: Read the CSV file and insert data into the 'adress' table
with open('adress.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        name, adress = row
        # Insert data into the table
        cursor.execute('INSERT INTO adress (adress, name) VALUES (?, ?)', (adress, name))

# Step 3: Commit the changes and close the connection
connection.commit()
connection.close()

print("CSV data inserted successfully into the 'adress' table.")