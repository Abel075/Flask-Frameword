from flask import Flask 
app = Flask(__name__)  

# Metodos 

# GET / POST / PUT / PATH / DELETE

@app.route('/post/<post_id>', methods=['GET', 'POST'])

def lala(post_id):
    return 'El id del post es: ' + post_id

