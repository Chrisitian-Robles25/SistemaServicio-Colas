from flask import Blueprint, jsonify, make_response,abort, request, render_template, redirect
#from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl

router = Blueprint('api', __name__)
    
@router.route('/')
def home():
    return render_template('template.html')

#Lista clientes
@router.route('/clientes')
def lista_clientes():
    cd = ClienteDaoControl()
    return render_template('clientes/lista.html', lista = cd.to_dict())

@router.route('/clientes/ver')
def ver_guardar():
    return render_template('clientes/guardar.html')

#editar personas
@router.route('/clientes/editar/<pos>')
def ver_editar(pos):
    pd = ClienteDaoControl()
    nene = pd._list().get(int(pos) -1)
    print(nene)
    return render_template("clientes/editar.html", data = nene )


#guardar personas
@router.route('/clientes/guardar', methods=["POST"])
def guardar_clientes():
    pd = ClienteDaoControl()
    data = request.form
    if not "apellido" in data.keys():
        abort(404)
    #TODO ...Validar
    pd._cliente._nombre = data["nombre"]
    pd._cliente._apellido = data["apellido"]
    pd._cliente._dni = data["dni"]
    pd._cliente._telefono = data["telefono"]
    pd._cliente._direccion = data["direccion"]
    pd._cliente._TiempoAtencion = data["tiempoAtencion"]
    pd._cliente._CalificarServicio = data["calificarServicio"]
    pd.save
    return redirect("/clientes", code=302)

@router.route('/clientes/modificar', methods=["POST"])
def modificar_clientes():
    pd = ClienteDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().get(int(data["id"]))
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._cliente = nene
    pd._cliente._nombre = data["nombre"]
    pd._cliente._apellido = data["apellido"]
    pd._cliente._dni = data["dni"]
    pd._cliente._telefono = data["telefono"]
    pd._cliente._direccion = data["direccion"]
    pd._cliente._TiempoAtencion = data["tiempoAtencion"]
    pd._cliente._CalificarServicio = data["calificarServicio"]
    pd.merge(int(pos) -1)
    return redirect("/clientes", code=302)

@router.route('/clientes/eliminar', methods=["POST"])
def eliminar_clientes():
    pd = ClienteDaoControl()
    pos = request.form["id"]
    pd._delete(int(pos))
    return redirect("/clientes", code=302)
                    