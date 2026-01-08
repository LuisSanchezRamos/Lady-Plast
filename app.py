from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "clave_secreta"

def conectar():
    return sqlite3.connect("login.db")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        session["usuario"] = usuario
        
        
        clave = request.form["clave"]

        con = conectar()
        cur = con.cursor()
        cur.execute(
            "SELECT id, clave, rol FROM usuario WHERE usuario = ?",
            (usuario,)
        )
        fila = cur.fetchone()
        con.close()

        if fila and check_password_hash(fila[1], clave):
            session["user_id"] = fila[0]    
            session["rol"] = fila[2]

            if fila[2] == "admin":
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("usuario"))

        return "❌ Usuario o clave incorrectos"

    return render_template("login.html")

# Ruta administrador
@app.route("/admin")
def admin():
    if "rol" not in session or session["rol"] != "admin":
        return redirect(url_for("login"))
    return render_template("admin.html")

# Ruta jefe produccion
@app.route("/Jefe-produccion")
def usuario():
    if "rol" not in session or session["rol"] != "encargada_produccion":
        return redirect(url_for("login"))
    return render_template("Jefe-produccion.html")

# logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)