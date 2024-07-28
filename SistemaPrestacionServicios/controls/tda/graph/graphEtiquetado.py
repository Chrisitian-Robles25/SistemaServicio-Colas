from controls.tda.graph.graphManaged import GraphManaged
from controls.exception.arrayPositionException import ArrayPositionException
import os.path
import os

class GraphEtiquetado(GraphManaged):
    def __init__(self, listaObjetos):
        self.__numVer = listaObjetos._lista._length
        super().__init__(self.__numVer)
        self.__labels = [None] * self.__numVer

        # Agrega los objetos de la lista enlazada a las etiquetas
        current = listaObjetos._lista.getNode(0)
        for i in range(self.__numVer):
            if current:
                self.__labels[i] = current._data
                current = current._next

    def addLabel(self, v, obj):
        if 0 <= v < self.num_vertex:
            self.__labels[v] = obj
        else:
            raise ArrayPositionException("Delimites out")

    def getLabel(self, v):
        if 0 <= v < self.num_vertex:
            return self.__labels[v]
        else:
            raise ArrayPositionException("Delimites out")

    def __str__(self):
        result = "Graph with labels:\n"
        for i in range(self.num_vertex):
            result += f"Vertex {i}: {self.__labels[i]}\n"
        return result

    def paint_graphLabel(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + "/static/d3/grafo.js"
        js = 'var nodes = new vis.DataSet([\n'
        
        # Añade los nodos con sus etiquetas
        for i in range(self.num_vertex):
            label = str(self.__labels[i])
            js += '{id: ' + str(i + 1) + ', label: "' + label + '"},\n'
        js += ']);\n'
        
        # Añade las aristas aun tiene errores
        js += 'var edges = new vis.DataSet([\n'
        for i in range(self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(adjs._length):
                    adj = adjs.get(j)
                    js += '{from: ' + str(i + 1) + ', to: ' + str(adj._destination + 1) + ', label: "' + str(adj._weight) + '"},\n'
        js += ']);\n'
        
        # Cierra el contenido de JavaScript
        js += 'var container = document.getElementById("mynetwork");\n'
        js += 'var data = {nodes: nodes, edges: edges};\n'
        js += 'var options = {};\n'
        js += 'var network = new vis.Network(container, data, options);\n'
        
        # Escribe el archivo JavaScript
        with open(url, "w") as file:
            file.write(js)
        
        print(f"Graph visualization saved to: {url}")