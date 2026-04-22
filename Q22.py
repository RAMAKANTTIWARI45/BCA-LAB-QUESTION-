# Q22: CRUD operations

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Insert
cursor.execute("INSERT INTO student VALUES(1, 'Ram')")

# Update
cursor.execute("UPDATE student SET name='Shyam' WHERE id=1")

# Select
cursor.execute("SELECT * FROM student")
print(cursor.fetchall())

# Delete
cursor.execute("DELETE FROM student WHERE id=1")

conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM student")
print(cursor.fetchall())

conn.close()