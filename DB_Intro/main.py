import sqlite3

conn = sqlite3.connect('film_database.db')
cursor = conn.cursor()

cursor.execute('select * FROM films WHERE release_year >= 2000')

# Fetch all rows
rows = cursor.fetchall()

# Print the titles of the films released in 2000 or later
for row in rows:
    print(row[1], row[2])

cursor.close()
conn.close()



