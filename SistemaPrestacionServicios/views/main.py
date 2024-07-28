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
busqueda = Dijkstra(oficina.obtenerGrafo, 6, 4)


oficina.obtenerGrafo  
print(oficina.caminoCorto(6, 4))