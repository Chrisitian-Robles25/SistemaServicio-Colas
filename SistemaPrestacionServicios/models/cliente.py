from models.persona import Persona
from models.enumCalificacion import EnumCalificacion

#cliente es una herencia de persona 
class Cliente(Persona):
    def __init__(self):
        super().__init__()
        self.__TiempoAtencion = ''
        self.__CalificarServicio = EnumCalificacion.BUENO
    
    @property
    def _TiempoAtencion(self):
        return self.__TiempoAtencion

    @_TiempoAtencion.setter
    def _TiempoAtencion(self, value):
        self.__TiempoAtencion = value

    @property
    def _CalificarServicio(self):
        return self.__CalificarServicio

    @_CalificarServicio.setter
    def _CalificarServicio(self, value):
        self.__CalificarServicio = value

    @property
    def serializar(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'dni': self._dni,
            'direccion': self._direccion,
            'telefono': self._telefono,
            'tiempo de atencion': self._TiempoAtencion,
            'calificarServicio': self._CalificarServicio
        }
    
    def deserializar(data):
        cliente = Cliente()
        cliente._id = data['id']
        cliente._nombre = data['nombre']
        cliente._apellido = data['apellido']
        cliente._dni = data['dni']
        cliente._direccion = data['direccion']
        cliente._telefono = data['telefono']
        cliente._TiempoAtencion = data['tiempo de atencion']
        cliente._CalificarServicio = data['calificarServicio']
        return cliente
    
    def __str__(self) -> str:
        return f'{self._id} {self._nombre} {self._apellido} {self._dni} {self._direccion} {self._telefono} {self.__CalificarServicio}'
        