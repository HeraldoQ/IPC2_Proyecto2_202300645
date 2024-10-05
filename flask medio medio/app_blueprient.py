from flask import Blueprint, render_template

app_blueprint = Blueprint('Ejemplo', __name__, template_folder='templates')

@app_blueprint.route('/inicio')
def inicio():
    return render_template('inicio.html')


@app_blueprint.route('/fin')
def fin():
    return render_template('fin.html')

@app_blueprint.route('/tabla')
def tabla():
    return render_template('tabla.html')




#se pone en el html el "segundos" para que se pueda usar en el html
@app_blueprint.route('/tabla/<numero>')
def tabla_numero(numero):
    context = {"segundos": numero}
    return render_template('tabla_numero.html', context=context)    

