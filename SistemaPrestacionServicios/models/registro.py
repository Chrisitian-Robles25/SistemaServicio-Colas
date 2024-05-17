from models.enumCalificacion import EnumCalificacion
from models.persona import Persona
class Registro:
    def __init__(self):
        self.__fecha = ''
        self.__servidor = Persona()
        self.__cliente = Persona()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _servidor(self):
        return self.__servidor

    @_servidor.setter
    def _servidor(self, value):
        self.__servidor = value

    @property
    def _cliente(self):
        return self.__cliente

    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value
  
    @property
    def serializar(self):
        return {
            'id': self.__id,
            'fecha': self.__fecha,
            'servidor': self.__servidor.serializar,
            'cliente': self.__cliente.serializar
        }
    
    def deserializar(data):
        registro = Registro()
        registro._id = data['id']
        registro._fecha = data['fecha']
        registro._servidor = Persona.deserializar(data['servidor'])
        registro._cliente = Persona.deserializar(data['cliente'])
        return registro
    
    def __str__(self) -> str:
        return f'{self.__id} {self.__fecha} {self.__servidor} {self.__cliente}'