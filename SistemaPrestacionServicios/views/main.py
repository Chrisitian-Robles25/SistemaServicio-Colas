import sys
import os

sys.path.append('../')
from time import time
import random

from controls.personaDaoControl import PersonaDaoControl
from controls.clienteDaoControl import ClienteDaoControl
from controls.registroDaoControl import RegistroDaoControl
from controls.tda.linked.linkedList import LinkedList
sys.setrecursionlimit(3000)  # El valor predeterminado suele ser 1000

#clienteDC = ClienteDaoControl()
#registroDC = RegistroDaoControl()

def load_random_numbers():
    numbers = []
    with open('random_numbers.txt', 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers
    
    random_numbers = [round(random.random() * 24999) for _ in range(24999)]
    with open('random_numbers.txt', 'w') as file:
        for number in random_numbers:
            file.write(f"{number}\n")

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split()
    return [int(number) for number in numbers]

try:
    lista = LinkedList()
    numbers = read_numbers_from_file('random_numbers.txt')
    for number in numbers:
        lista.add(number)

    Inicio = time()
    
    lista.sort(1)
    lista.print
    
    FIN = time()
    Total = FIN - Inicio
    print(f"El tiempo de ejecución del programa es: {Total} segundos")

except Exception as error:
    print(error.args)

    """ clienteDC._cliente._nombre = "Christian"
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
    clienteDC._lista._lenghtLista_
    print("El tamaño de la lista es: ", clienteDC._lista._lenghtLista_, "kilobytes") """











    #registroDC._lista._lenghtLista_
    #print("El tamaño de la lista es: ", registroDC._lista._lenghtLista_, "kilobytes")

      

    """ registroDC._registro._servidor = "V1-Wilman Sanchez"
    registroDC._registro._fecha = "18/05/2024"
    registroDC._registro._clienteDni = "1105549602"
    registroDC.save
    
    registroDC._registro._servidor = "V1-Wilman Sanchez"
    registroDC._registro._fecha = "18/05/2024"
    registroDC._registro._clienteDni = "0778465219"
    registroDC.save

    registroDC._registro._servidor = "V1-Wilman Sanchez"
    registroDC._registro._fecha = "18/05/2024"
    registroDC._registro._clienteDni = "1978495614"
    registroDC.save """