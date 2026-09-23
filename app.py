from flask import Flask,render_template,request,make_response,url_for,session,redirect

app=Flask(__name__)
app.secret_key="una_clave_secreta"

usuarios={
    "carlos":"1111",
    "laura":"2222",
    "diego":"3333"
}
lista_libros = [
    {"titulo": "Python desde cero", "autor": "Juan Pérez", "disponibles": 4},
    {"titulo": "Desarrollo Web", "autor": "María López", "disponibles": 2},
    {"titulo": "Inteligencia Artificial", "autor": "Pedro García", "disponibles": 0}
]

@app.route("/")
def inicio():
    ultimo_usuario = request.cookies.get("ultimo_usuario")
    mensaje = request.args.get("mensaje")
    return render_template("index.html", ultimo_usuario=ultimo_usuario, mensaje=mensaje)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario in usuarios and usuarios[usuario] == password:
            session["usuario"] = usuario
            resp = make_response(redirect(url_for("libros")))
            resp.set_cookie("ultimo_usuario", usuario)
            return resp
        else:
            error = "Usuario o contraseña incorrectos."

    return render_template("login.html", error=error)

@app.route("/libros")
def libros():
    return render_template("libros.html", libros=lista_libros)

@app.route("/perfil")
def perfil():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("perfil.html", usuario=session["usuario"])

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("inicio", mensaje="sesion_cerrada"))
@app.route("/eliminar-cookie")
def eliminar_cookie():
    resp = make_response(redirect(url_for("inicio")))
    resp.delete_cookie("ultimo_usuario")
    return resp

if __name__=="__main__":
    app.run(debug=True)