import sys
sys.path.append('../')

from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl
from controls.registroDaoControl import RegistroDaoControl
from controls.tda.queque.queque import Queque
from controls.tda.arrayList.arrayList import ArrayList
#persona = Persona()
#personaDC = PersonaDaoControl()
#CREAR UN OBJETO PARA DARLE QUEQUE Con un tamaño de 5
#queque = Queque(3)
clienteDC = ClienteDaoControl()
registroDC = RegistroDaoControl()
#myList = ArrayList()
try:

    clienteDC._cliente._nombre = "Christian"
    clienteDC._cliente._apellido = "Robles"
    clienteDC._cliente._dni = "1105549602"
    clienteDC._cliente._direccion = "Alamor"
    clienteDC._cliente._telefono = "0991745767"
    clienteDC._cliente._TiempoAtencion = "00:25"
    clienteDC._cliente._CalificarServicio = "Excelente"
    clienteDC.save
    #queque.queque(clienteDC)
    #myList.__addFirst__(clienteDC)
    clienteDC._cliente._nombre = "Esteban"
    clienteDC._cliente._apellido = "Leon"
    clienteDC._cliente._dni = "0778465219"
    clienteDC._cliente._direccion = "Pinas"
    clienteDC._cliente._telefono = "0978461578"
    clienteDC._cliente._TiempoAtencion = "01:12"
    clienteDC._cliente._CalificarServicio = "Malo"
    clienteDC.save
    #queque.queque(clienteDC)
    #myList.__addLast__(clienteDC)

    clienteDC._cliente._nombre = "Santiago"
    clienteDC._cliente._apellido = "Tamayo"
    clienteDC._cliente._dni = "1978495614"
    clienteDC._cliente._direccion = "Colombia"
    clienteDC._cliente._telefono = "0978461385"
    clienteDC._cliente._TiempoAtencion = "00:45"
    clienteDC._cliente._CalificarServicio = "Regular"
    clienteDC.save
    #queque.queque(clienteDC)
    

    registroDC._registro._servidor = "V1-Wilman Sanchez"
    registroDC._registro._fecha = "18/05/2024"
    registroDC._registro._clienteDni = "1105549602"
    registroDC.save


    #queque.queque(clienteDC)
    #print (queque)
except Exception as error:
    print(error.args)