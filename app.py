from flask import Flask, render_template,request,make_response,url_for,sessions


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/libros")
def libros():
    return render_template("libros.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/logout")
def logout():
    return "Sesion cerrada"

if __name__ == "__main__":
    app.run(debug=True)