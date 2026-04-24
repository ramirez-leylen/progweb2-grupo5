# importa libreria Flask
from flask import Flask

# importa lal funcion escape de la libreria markupsafe
from markupsafe import escape

# crea instancia de la clase Flask
# le indica a Flask donde encontrar recursos
app = Flask(__name__)



# hello world
# en la ruta /holamundo, corre la funcion hello_world
@app.route('/holamundo')
def hello_world():
    return 'Hola mundo'



# ruta con formato
@app.route('/formato')
def formato():
    return '<h1>Aplicación con formato</h1>'



# filtro de seguridad
# evita ataques de inyeccion
@app.route('/<name>')
def hello_name(name):
    return f'Hello {escape(name)}'



# sin escape
# @app.route('/<name>')
# def hello(name):
#     return f'Hello {name}'



# mas ejemplos de enrutamiento
@app.route('/')
def index():
    return 'Index Page'



@app.route('/hello')
def hello():
    return 'Hello, World'