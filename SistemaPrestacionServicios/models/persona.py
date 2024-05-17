class Persona():
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__apellido = ''
        self.__dni = ''
        self.__direccion = ''
        self.__telefono = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def serializar(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'dni': self.__dni,
            'direccion': self.__direccion,
            'telefono': self.__telefono
        }

    def deserializar(data):
        persona = Persona()
        persona._id = data['id']
        persona._nombre = data['nombre']
        persona._apellido = data['apellido']
        persona._dni = data['dni']
        persona._direccion = data['direccion']
        persona._telefono = data['telefono']
        return persona
    
    def __str__(self) -> str:
        return f'Persona: {self.__nombre} {self.__apellido}'