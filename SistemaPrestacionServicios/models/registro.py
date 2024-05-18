from models.enumCalificacion import EnumCalificacion
from models.persona import Persona

class Registro:
    def __init__(self):
        self.__fecha = ''
        self.__servidor = '' 
        self.__clienteDni = ''

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
    def _clienteDni(self):
        return self.__clienteDni

    @_clienteDni.setter
    def _clienteDni(self, value):
        self.__clienteDni = value
  
    @property
    def serializar(self):
        return {
            'id': self.__id,
            'fecha': self.__fecha,
            'servidor': self.__servidor,
            'clienteDni': self.__clienteDni
        }
    
    def deserializar(data):
        registro = Registro()
        registro._id = data['id']
        registro._fecha = data['fecha']
        registro._servidor = data['servidor']
        registro._clienteDni = data['clienteDni']
        return registro
    
    def __str__(self) -> str:
        return f'{self.__id} {self.__fecha} {self.__servidor} {self.__clienteDni}'