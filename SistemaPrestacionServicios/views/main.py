import sys
sys.path.append('../')
from controls.tda.linked.linkedList import LinkedList
from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl
from controls.registroDaoControl import RegistroDaoControl
from controls.tda.queque.queque import Queque

#persona = Persona()
personaDC = PersonaDaoControl()
clienteDC = ClienteDaoControl()
registroDC = RegistroDaoControl()
try:
    personaDC._persona._nombre = "jose"
    personaDC._persona._apellido = "guaman"
    personaDC._persona._dni = "1105549601"
    personaDC._persona._direccion = "loja 123"
    personaDC._persona._telefono = "0987654321"
    personaDC.save
    personaDC._persona._nombre = "franco"
    personaDC._persona._apellido = "salcedo"
    personaDC._persona._dni = "1105549602"
    personaDC._persona._direccion = "quito 123"
    personaDC._persona._telefono = "0987654322"
    personaDC.save
    
    clienteDC._cliente._nombre = "Christian"
    clienteDC._cliente._apellido = "Robles"
    clienteDC._cliente._dni = "1105549602"
    clienteDC._cliente._direccion = "alamor 123"
    clienteDC._cliente._telefono = "0987654321"
    clienteDC._cliente._CalificarServicio = "BUENO"
    clienteDC.save
    clienteDC._cliente._nombre = "esteban"
    clienteDC._cliente._apellido = "leon"
    clienteDC._cliente._dni = "1105549603"
    clienteDC._cliente._direccion = "pinas 321"
    clienteDC._cliente._telefono = "0987654322"
    clienteDC._cliente._CalificarServicio = "MALO"
    clienteDC.save

except Exception as error:
    print(error.args)