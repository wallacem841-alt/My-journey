import sqlite3
import time

start_time = time.time()

def initialize_database():
    conn = sqlite3.connect('nutrition_tracker.db')
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute('PRAGMA foreign_keys = ON;')

    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS food_db (
        name TEXT PRIMARY KEY,
        weight REAL NOT NULL,
        protein REAL NOT NULL,
        carbs REAL NOT NULL,
        fat REAL NOT NULL,
        kalories REAL NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS meals_db (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        meal TEXT NOT NULL,
        food TEXT NOT NULL,
        weight REAL NOT NULL,
        protein REAL NOT NULL,
        carbs REAL NOT NULL,
        fat REAL NOT NULL,
        kalories REAL NOT NULL,
        FOREIGN KEY (food) REFERENCES food_db (name)
    )
    ''')

    conn.commit()
    conn.close()

initialize_database()

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.5f} seconds")