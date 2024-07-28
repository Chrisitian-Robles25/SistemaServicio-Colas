from controls.dao.daoAdapter import DaoAdapter
from models.oficina.oficina import Oficina

class OficinaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Oficina)
        self.__oficina = None

    @property
    def _oficina(self):
        if self.__oficina == None:
            self.__oficina = Oficina()
        return self.__oficina

    @_oficina.setter
    def _oficina(self, value):
        self.__oficina = value
    
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._oficina._id = self._lista._lenght + 1
        self._save(self._oficina)
    
    def merge(self, pos):
        self._merge(self._oficina, pos)

    def delete(self, pos):
        self._delete(self._oficina, pos)