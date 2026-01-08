import sqlite3

con = sqlite3.connect("login.db")
cur = con.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                clave TEXT NOT NULL,
                rol TEXT NOT NULL
            )
            """)
con.commit()
con.close()

print("BD creada con roles")