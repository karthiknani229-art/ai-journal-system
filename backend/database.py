import sqlite3

def init_db():
    conn = sqlite3.connect("journal.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        emotion TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()