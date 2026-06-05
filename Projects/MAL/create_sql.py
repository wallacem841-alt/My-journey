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

conn.commit()

conn.close()