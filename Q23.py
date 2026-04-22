# Q23: Transaction

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO student VALUES(2, 'Mohan')")
    conn.commit()
    print("Transaction successful")
except:
    conn.rollback()
    print("Transaction failed")

conn.close()