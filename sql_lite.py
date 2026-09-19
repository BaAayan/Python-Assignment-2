import sqlite3

conn = sqlite3.connect("school.db")      # 1. open (or create) the database
cur = conn.cursor()                      # 2. create a cursor

try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            grade INTEGER
        )
    """)

    # 3. insert data using ? placeholders (safe from SQL injection)
    cur.execute("INSERT INTO students (name, grade) VALUES (?, ?)",
                ("Tendai Moyo", 5))
    cur.executemany("INSERT INTO students (name, grade) VALUES (?, ?)",
                    [("Rudo Chikwanha", 4), ("Farai Ncube", 6)])

    conn.commit()                        # 4. make the changes permanent

    # 5. query the data
    cur.execute("SELECT id, name, grade FROM students WHERE grade >= ?", (5,))
    for row in cur.fetchall():
        print(row)

except sqlite3.Error as err:
    conn.rollback()                      # undo the transaction on failure
    print("Database error:", err)

finally:
    conn.close()                         # 6. always release the connection