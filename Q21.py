# Q21: Create database and table

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER, name TEXT)")

print("Table created successfully")

conn.close()
import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

conn.close()