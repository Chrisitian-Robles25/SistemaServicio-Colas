from flask import Blueprint, jsonify, make_response,abort, request, render_template, redirect

#from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl
from controls.registroDaoControl import RegistroDaoControl


router = Blueprint('api', __name__)


@router.route('/')
def home():
    return render_template('template.html')

#Lista clientes
@router.route('/clientes')
def lista_clientes():
    cd = ClienteDaoControl()
    list = cd._list()
    list.sort_models("_id",1)
    return render_template('clientes/lista.html', lista = cd.to_dic_lista(list))

@router.route('/clientes/<int:tipo>/<attr>/<int:metodo>')
def lista_clientes_ordenar(tipo, attr, metodo):
    cd = ClienteDaoControl()
    list = cd._list()
    list.sort_models(attr, tipo, metodo)
    #return render_template('clientes/lista.html', lista = cd.to_dict_lista(list))
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": cd.to_dic_lista(list)}),
        200
    )

@router.route('/clientes/search/<string:elemento>/<string:attr>')
def lista_clientes_search(elemento, attr):
    cd = ClienteDaoControl()
    list = cd._list()
    if attr == '_dni' or attr == '_telefono':
        list.search_binary_models(elemento, attr)
    list.search_binarySecuencial_models(elemento, attr)
    print(cd._transform_())
    return make_response(jsonify({"msg":"OK", "code": 200, "data":cd.to_dic_lista(list)}),)






@router.route('/registros')
def lista_registros():
    rd = RegistroDaoControl()
    return render_template('registros/lista.html', lista = rd.to_dict())

@router.route('/registros/<int:tipo>/<attr>/<int:metodo>')
def lista_registros_ordenar(tipo, attr, metodo):
    cd = RegistroDaoControl()
    list = cd._list()
    list.sort_models(attr, tipo, metodo)
    #return render_template('clientes/lista.html', lista = cd.to_dict_lista(list))
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": cd.to_dic_lista(list)}),
        200
    )

@router.route('/registros/search/<string:elemento>/<string:attr>')
def lista_registros_search(elemento, attr):
    cd = RegistroDaoControl()
    list = cd._list()
    if attr == '_clienteDni':
        list.search_binary_models(elemento, attr)
    list.search_binarySecuencial_models(elemento, attr)
    print(cd._transform_())
    return make_response(jsonify({"msg":"OK", "code": 200, "data":cd.to_dic_lista(list)}),)







@router.route('/clientes/ver')
def ver_guardar():
    return render_template('clientes/guardar.html')

@router.route('/registros/ver')
def ver_guardar2():
    return render_template('registros/guardar.html')

#editar personas
@router.route('/clientes/editar/<pos>')
def ver_editar(pos):
    pd = ClienteDaoControl()
    print("ID NENE" + str(pos))
    nene = pd._get(int(pos)) #pd._list().get(int(pos) -1)
    print(nene)
    return render_template("clientes/editar.html", data = nene )

@router.route('/registros/editar/<pos>')
def ver_editar2(pos):
    pd = RegistroDaoControl()
    nene = pd._list().get(int(pos) -1)
    print(nene)
    return render_template("registros/editar.html", data = nene )

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

@router.route('/registros/guardar', methods=["POST"])
def guardar_registros():
    pd = RegistroDaoControl()
    data = request.form
    if not "servidor" in data.keys():
        abort(404)
    #TODO ...Validar
    pd._registro._servidor = data["servidor"]
    pd._registro._fecha = data["fecha"]
    pd._registro._clienteDni = data["clienteDni"]
    pd.save
    return redirect("/registros", code=302)

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

@router.route('/registros/modificar', methods=["POST"])
def modificar_registros():
    pd = RegistroDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().get(int(data["id"]))
    if not "servidor" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._registro = nene
    pd._registro._servidor = data["servidor"]
    pd._registro._fecha = data["fecha"]
    pd._registro._clienteDni = data["clienteDni"]
    pd.merge(int(pos) -1)
    return redirect("/registros", code=302)

@router.route('/clientes/eliminar', methods=["POST"])
def eliminar_clientes():
    pd = ClienteDaoControl()
    pos = request.form["id"]
    pd._delete(int(pos))
    return redirect("/clientes", code=302)
                    