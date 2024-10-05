from flask import Flask, request
from app_blueprient import app_blueprint



app = Flask(__name__)
app.register_blueprint(app_blueprint)


@app.route('/get', methods=['GET'])
def perticion_get():
    print("Hola Mundo")
    return "<h2>Hello World get<h2>"





@app.route('/post', methods=['POST'])
def peticion_post():
    nombre = request.json["nombre"]
    print(nombre)
    return f"<h2>El nombre es: <strong> { nombre }  </strong></h2>"
    



    

@app.route('/get/<id>', methods=['GET'])
def _peticion_get2(id):
    print(id)
    return f"<p>El ID es <strong>{id} </strong> </p>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)


