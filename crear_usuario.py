import sqlite3
from werkzeug.security import generate_password_hash

con = sqlite3.connect("login.db")
cur = con.cursor()

usuarios = [
    ("", generate_password_hash(""), ""),
    ("", generate_password_hash(""), "")
]

cur.executemany(
    "INSERT INTO usuario (usuario, clave, rol) VALUES (?, ?, ?)",
    usuarios
)

con.commit()
con.close()

print("Usuarios creados")