import sqlite3
from werkzeug.security import generate_password_hash

con = sqlite3.connect("login.db")
cur = con.cursor()

usuarios = [
    ("admin", generate_password_hash("1234"), "admin"),
    ("Paola", generate_password_hash("1234"), "encargada_produccion")
]

cur.executemany(
    "INSERT INTO usuario (usuario, clave, rol) VALUES (?, ?, ?)",
    usuarios
)

con.commit()
con.close()

print("Usuarios creados")