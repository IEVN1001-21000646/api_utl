from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    titulo='IEVN-1001'
    list=['Juan','Luis','Fulanito']
    return render_template('uno.html', titulo=titulo, list=list)


@app.route("/user/<string:user>")

def user(user):
    return "El usuario es: {}".format(user)

@app.route("/user/<int:n1>")

def numero(n1):
    return "El numero es: {}".format(n1)

@app.route("/user/<string:nom>/<int:id>")

def idNom(nom,id):
    return " <h1> ID: {} Nombre: {}".format(id, nom)

@app.route("/suma/<float:n1>/<float:n2>")

def float1(n1,n2):
    return "La suma es: {}".format(n2+n1)

@app.route("/default")
@app.route("/default/<string:nom>")

def nom2(nom='Kas'):
    return "El nombre es: {}".format(nom)


if __name__=="__main__":
    app.run(debug=True)