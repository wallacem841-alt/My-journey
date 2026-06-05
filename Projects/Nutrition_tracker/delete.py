import sqlite3

def delete_meal(ids):
    conn = sqlite3.connect('nutrition_tracker.db')
    cursor = conn.cursor()

    for i in ids:
        try:
            cursor.execute('DELETE FROM meals_db WHERE id = ?', (i,))

        except sqlite3.DatabaseError:
            conn.close()
            return 'DatabaseError'
        
    conn.commit()
    conn.close()

    return 0

# Example usage

test = delete_meal([6,7])

print(test)