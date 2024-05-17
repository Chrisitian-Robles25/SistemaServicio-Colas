from models.registro import Registro

class RegistroControl():
    def __init__(self):
        self.__registro = Registro()
    
    @property
    def _registro(self):
        return self.__registro
    
    @_registro.setter
    def _registro(self, value):
        self.__registro = value
    
    def _serializar(self):
        return self.__registro.serializar
    
    def _deserializar(data):
        return Registro.deserializar(data)
    
    def __str__(self) -> str:
        return str(self.__registro)
    
    def __repr__(self) -> str:
        return str(self.__registro)
    
    def _save(self):
        self._save(self.__registro)

    def __str__(self) -> str:
        return str(self.__registro)