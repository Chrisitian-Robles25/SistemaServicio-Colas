class Oficina():
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre = ""
        self.__direccion = "s/n"
        self.__horario = "s/n"
        self.__lng = '0.0'
        self.__lat = '0.0'

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
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _horario(self):
        return self.__horario

    @_horario.setter
    def _horario(self, value):
        self.__horario = value

    @property
    def _lng(self):
        return self.__lng

    @_lng.setter
    def _lng(self, value):
        self.__lng = value

    @property
    def _lat(self):
        return self.__lat

    @_lat.setter
    def _lat(self, value):
        self.__lat = value

    def __str__(self) -> str:
        return str(self.__id) + ' ' + self.__nombre
    
    @property
    def serializar(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "direccion": self.__direccion,
            "horario": self.__horario,
            "lng": self.__lng, 
            "lat": self.__lat
        }
    
    def deserializar(data):
        oficina = Oficina()
        oficina._id = data["id"]
        oficina._nombre = data["nombre"]
        oficina._direccion = data["direccion"]
        oficina._horario = data["horario"]
        oficina._lng = data["lng"]
        oficina._lat = data["lat"]
        return oficina