from flask import Blueprint, jsonify, make_response,abort, request, render_template, redirect

#from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl
from controls.registroDaoControl import RegistroDaoControl
from controls.oficina.oficinaDaoControl import OficinaDaoControl
from controls.oficina.oficinaGrafo import OficinaGrafo
from controls.tda.graph.metodoBusqueda.dijkstra import Dijkstra

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

@router.route('/oficinas/<tipo>/<attr>/<metodo>')
def lista_oficinas_ordenar(tipo, attr=0, metodo=0):
    pd = OficinaDaoControl()
    list = pd._list()
    if list.isEmpty:
        return make_response(
            jsonify({"msg":"NO DATA", "code": 200, "data": []}),
            404
        )
    list.sort_models(attr, int(tipo), int(metodo))
    #return render_template("nene/lista.html", lista=pd.to_dic_lista(list))
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": pd.to_dic_lista(list)}),
        200
    )

@router.route('/grafo')
def grafo():
    return render_template("d3/grafo.html")

""" @router.route('/grafo/busqueda/<origen>/<destino>')
def grafo_busqueda(origen, destino):
    ng = OficinaGrafo()
    ng.obtenerGrafo
    camino, distancia = ng.caminoCorto(int(origen), int(destino))
    
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": {"camino": camino, "distancia": distancia}}),
        200
    ) """

@router.route('/grafo_oficina/<origen>/<destino>/<algoritmo>')
def grafo_oficina(origen, destino, algoritmo):
    try:
        origen = int(origen)
        destino = int(destino)
        algoritmo = int(algoritmo)
    except ValueError:
        return make_response(
            jsonify({"msg": "Invalid input. Parameters must be integers.", "code": 400}),
            400
        )

    pd = OficinaDaoControl()
    ng = OficinaGrafo()
    grafo = ng.obtenerGrafo
    grafo.paint_graph()
    list = pd._list()
    #id_to_nombre = {item.id: item.nombre for item in list}
    camino, distancia = ng.caminoCorto(origen, destino, algoritmo)
    return render_template("d3/grafo.html", lista=pd.to_dic_lista(list), caminoCorto=camino, Distancia=distancia)


@router.route('/grafo_ver_admin')
def grafo_ver_admin():
    pd = OficinaDaoControl()
    grafoNegocio = OficinaGrafo()
    grafoNegocio.obtenerGrafo
    list = pd._list()
    if not list.isEmpty:
        list.sort_models("_nombre", 2)

    json = grafoNegocio.obtainWeigth
    grafoNegocio.__str__()
    print(json)
    return render_template("oficina/grafo.html", lista=pd.to_dic_lista(list), grafonegocioaux=json)

@router.route('/oficinas/agregar-adjancencia', methods=["POST"])
def lista_oficinas_get():
    data = request.form
    negGraph = OficinaGrafo()
    """grafo = negGraph.create_graph()
    grafo.insert_edges(int(data["origen"]), int(data["destino"]))"""
    print(data)
    negGraph.obtenerGrafo.insert_edges(int(data["origen"])-1, int(data["destino"])-1)
    negGraph.save_graph
    return redirect("/grafo_ver_admin", code=302)

@router.route('/oficinas')
def lista_oficinas():
    pd = OficinaDaoControl()
    list = pd._list()
    if list.isEmpty:
        return render_template("oficina/lista.html")
    list.sort_models("_id", 1)
    return render_template("oficina/lista.html", lista=pd.to_dic_lista(list))

@router.route('/oficinas/ver')
def ver_guardar3():
    return render_template('oficina/guardar.html')

@router.route('/oficinas/editar/<pos>')
def ver_editar3(pos):
    pd = OficinaDaoControl()
    nene = pd._list().get(int(pos) -1)
    print(nene)
    return render_template("oficina/editar.html", data = nene )

@router.route('/oficinas/guardar', methods=["POST"])
def guardar_oficina():
    pd = OficinaDaoControl()
    data = request.form
    if not "nombre" in data.keys():
        abort(404)
    #TODO ...Validar
    pd._oficina._nombre = data ["nombre"]
    pd._oficina._direccion = data ["direccion"]
    pd._oficina._horario = data["horario"]
    pd._oficina._lng = float(data["lng"])
    pd._oficina._lat = float(data["lat"])
    pd.save
    return redirect("/oficinas", code=302)

@router.route('/oficinas/modificar', methods=["POST"])
def modificar_oficina():
    pd = OficinaDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().get(int(data["id"]))
    if not "nombre" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._oficina = nene
    pd._oficina._nombre = data ["nombre"]
    pd._oficina._direccion = data ["direccion"]
    pd._oficina._horario = data["horario"]
    pd._oficina._lng = data["lng"]
    pd._oficina._lat = data["lat"]
    pd.merge(int(pos) -1)
    return redirect("/oficinas", code=302)

@router.route('/oficinas/eliminar', methods=["POST"])
def eliminar_oficinas():
    pd = OficinaDaoControl()
    pos = request.form["id"]
    pd._delete(int(pos))
    return redirect("/oficinas", code=302)