#Importar el módulo Flask en el proyecto.
from flask import Flask,render_template

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/")
def home():
    name="Karla"
    age="17"

    return render_template("index.html",name=name,age=age)

@app.route("/")
def dad():
    name="Eduardo"
    age="45"

    return render_template("dad.html",name=name,age=age)

@app.route("/")
def mom():
    name="Yesenia"
    age="42"

    return render_template("mom.html",name=name,age=age)

@app.route("/")
def friend():
    name="Samantha"
    age="17"

    return render_template("friend.html",name=name,age=age)

#‘/’ URL está vinculado con la función first_flask.
def first_flask():

    return "Este es mi primer programa en Flask"

#Ejecutamos la app en el servidor local.
app.run()
