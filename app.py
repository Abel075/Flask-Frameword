from flask import Flask # Importacion de clase para crear ala aplicacion
app = Flask(__name__)  #Variable que sera main en ejecucion pero si se importa en otro archivo tendra el nombre de 'holamundo'

# set FLASK_APP=app.py
# flask run



# Decoradores @
@app.route('/')
def index():
    return 'hola mundo'

    

 #export FLASK_ENV=development para ver cambios en el servidor
# @app.route('/lala')
# def lala():
#     return 'hola lala'

    
