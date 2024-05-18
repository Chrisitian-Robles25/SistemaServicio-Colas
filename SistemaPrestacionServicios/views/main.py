import sys
sys.path.append('../')

from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl
from controls.registroDaoControl import RegistroDaoControl
from controls.tda.queque.queque import Queque

#persona = Persona()
#personaDC = PersonaDaoControl()
#CREAR UN OBJETO PARA DARLE QUEQUE Con un tamaño de 5
#queque = Queque(3)
clienteDC = ClienteDaoControl()
registroDC = RegistroDaoControl()
try:

    clienteDC._cliente._nombre = "Christian"
    clienteDC._cliente._apellido = "Robles"
    clienteDC._cliente._dni = "123456789"
    clienteDC._cliente._direccion = "Calle 123"
    clienteDC._cliente._telefono = "123456789"
    clienteDC._cliente._TiempoAtencion = "10 minutos"
    clienteDC._cliente._CalificarServicio = "Bueno"
    clienteDC.save
    #queque.queque(clienteDC)
    
    clienteDC._cliente._nombre = "Esteban"
    clienteDC._cliente._apellido = "Quito"
    clienteDC._cliente._dni = "123456789"
    clienteDC._cliente._direccion = "Av. el limon"
    clienteDC._cliente._telefono = "123456789"
    clienteDC._cliente._TiempoAtencion = "12 minutos"
    clienteDC._cliente._CalificarServicio = "Malo"
    clienteDC.save
    #queque.queque(clienteDC)

    clienteDC._cliente._nombre = "Juan"
    clienteDC._cliente._apellido = "Perez"
    clienteDC._cliente._dni = "123456789"
    clienteDC._cliente._direccion = "Calle 123"
    clienteDC._cliente._telefono = "123456789"
    clienteDC._cliente._TiempoAtencion = "10 minutos"
    clienteDC._cliente._CalificarServicio = "Bueno"
    clienteDC.save
    #queque.queque(clienteDC)

    registroDC._registro._servidor = "SERVIDOR 1 - JUANCHO"
    registroDC._registro._fecha = "10/24/2021"
    registroDC._registro._clienteDni = "123456789"
    #registroDC.save


    #queque.queque(clienteDC)
    #print (queque)
except Exception as error:
    print(error.args)