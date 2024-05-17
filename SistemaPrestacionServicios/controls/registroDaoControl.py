from controls.dao.daoAdapter import DaoAdapter
from models.registro import Registro

class RegistroDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Registro)
        self.__registro = None
    
    @property
    def _registro(self):
        if self.__registro == None:
            self.__registro = Registro()   
        return self.__registro
    
    @_registro.setter
    def _registro(self, value):
        self.__registro = value
    
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._registro._id = self._lista._lenght + 1
        self._save(self._registro)

    def merge(self, pos):
        self._merge(self._registro, pos)
    
    def delete(self, pos):
        self._delete(self._registro, pos)
    
    #crear el str
    def str(self):
        return self._registro._nombre + " " + self._registro._apellido + " " + self._registro._dni + " " + self._registro._direccion + " " + self._registro._telefono