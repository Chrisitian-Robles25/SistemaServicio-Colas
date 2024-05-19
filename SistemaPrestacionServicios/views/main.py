import sys
import os
import psutil
sys.path.append('../')
from time import time

from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl
from controls.registroDaoControl import RegistroDaoControl
from controls.tda.queque.queque import Queque
from controls.tda.arrayList.arrayList import ArrayList

clienteDC = ClienteDaoControl()
registroDC = RegistroDaoControl()
try:
    Inicio = time()
    clienteDC._cliente._nombre = "Christian"
    clienteDC._cliente._apellido = "Robles"
    clienteDC._cliente._dni = "1105549602"
    clienteDC._cliente._direccion = "Alamor"
    clienteDC._cliente._telefono = "0991745767"
    clienteDC._cliente._TiempoAtencion = "00:25"
    clienteDC._cliente._CalificarServicio = "Excelente"
    clienteDC.save
    
    clienteDC._cliente._nombre = "Esteban"
    clienteDC._cliente._apellido = "Leon"
    clienteDC._cliente._dni = "0778465219"
    clienteDC._cliente._direccion = "Pinas"
    clienteDC._cliente._telefono = "0978461578"
    clienteDC._cliente._TiempoAtencion = "01:12"
    clienteDC._cliente._CalificarServicio = "Malo"
    clienteDC.save

    clienteDC._cliente._nombre = "Santiago"
    clienteDC._cliente._apellido = "Tamayo"
    clienteDC._cliente._dni = "1978495614"
    clienteDC._cliente._direccion = "Colombia"
    clienteDC._cliente._telefono = "0978461385"
    clienteDC._cliente._TiempoAtencion = "00:45"
    clienteDC._cliente._CalificarServicio = "Regular"
    clienteDC.save    

    #Se calcula el tiempo de ejecución del programa
    FIN = time()
    Total = FIN - Inicio
    print(f"El tiempo de ejecución del programa es: {Total} segundos")

    # Calcula la memoria utilizada
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 ** 2
    print(f"La memoria utilizada por el programa es: {memory_usage} MB")
    
except Exception as error:
    print(error.args)

    #registroDC._registro._servidor = "V1-Wilman Sanchez"
    #registroDC._registro._fecha = "18/05/2024"
    #registroDC._registro._clienteDni = "1105549602"
    #registroDC.save