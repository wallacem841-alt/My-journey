import sqlite3

conn = sqlite3.connect('anime_list.db')

conn.execute('''
    CREATE TABLE series (
        id INTEGER PRIMARY KEY,
        type TEXT,
        entries INTEGER,
        title_east TEXT,
        title_west TEXT,
        image_path TEXT,
        rating INTEGER,
        tags TEXT,
        description_path TEXT
    )
''')

conn.execute('''
    CREATE TABLE Vedita1331 (
        id INTEGER PRIMARY KEY,
        series_id INTEGER,
        user_rating INTEGER,
        status TEXT,
        entries INTEGER
    )
''')
conn.execute('''
    INSERT INTO anime (title, image_path, rating, status)
    VALUES ('Naruto', '/images/naruto.jpg', 5, 'watching')
''')

conn.commit()

cursor = conn.execute('SELECT * FROM anime')
for row in cursor:
    print(row)

conn.execute("DELETE FROM anime WHERE title = 'Naruto'")
conn.commit()

cursor = conn.execute('SELECT * FROM anime')
for row in cursor:
    print(row)

conn.close()