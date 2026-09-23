from flask import Flask,render_template,request,make_response,url_for,session,redirect

app=Flask(__name__)
app.secret_key="una_clave_secreta"

usuarios={
    "carlos":"1111",
    "laura":"2222",
    "diego":"3333"
}

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    error=None

    if request.method=="POST":
        usuario=request.form["usuario"]
        password=request.form["password"]

        if usuario in usuarios and usuarios[usuario]==password:
            session["usuario"]=usuario
            return redirect(url_for("libros"))
        else:
            error="Usuario o contraseña incorrectos"

    return render_template("login.html",error=error)

@app.route("/libros")
def libros():
    return render_template("libros.html")

@app.route("/perfil")
def perfil():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("perfil.html",usuario=session["usuario"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)