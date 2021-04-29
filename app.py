from flask import Flask # Importacion de clase para crear ala aplicacion
app = Flask(__name__)  #Variable que sera main en ejecucion pero si se importa en otro archivo tendra el nombre de 'holamundo'



# Decoradores @
@app.route('/')
def index():
    return 'hola mundo'

    