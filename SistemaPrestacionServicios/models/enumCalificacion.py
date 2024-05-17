import enum

class EnumCalificacion(enum.Enum):
    MALO = 0
    REGULAR = 1
    BUENO = 2
    MUY_BUENO = 3
    EXCELENTE = 4

    def getInstance(self):
        if self.instance == None:
            self.instance = EnumCalificacion()
        return self.instance