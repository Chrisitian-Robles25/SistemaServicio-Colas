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
from controls.tda.graph.metodoBusqueda.dijkstra import Dijkstra
from controls.oficina.oficinaGrafo import OficinaGrafo


oficina = OficinaGrafo()

""" Inicio = time()
print("---------BUSCANDO CON DJIKSTRA---------")
oficina.obtenerGrafo 
print(oficina.caminoCorto(13, 12,1))
Findijkstra = time() - Inicio """
print("---------BUSCANDO CON FLOYD---------")
Inicio = time()
oficina.obtenerGrafo 
print(oficina.caminoCorto(13, 12,2))
Finfloyd = time() - Inicio


print(f"Tiempo de ejecución de Floyd: {Finfloyd}")

#print(f"Tiempo de ejecución de Dijkstra: {Findijkstra}")

