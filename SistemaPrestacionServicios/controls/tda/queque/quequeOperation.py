from controls.tda.linked.linkedList import LinkedList #importanmos linkedList porque ya tenemos los metodos de la lista enlazada

class QuequeOperation(LinkedList):
    def __init__(self, top):
        super().__init__()
        self.__top = top

    @property
    def get_top(self):
        return self.__top

    def set_top(self, value):
        self.__top = value

    @property
    def verifyTop(self):
        return self._lenght < self.__top

    def queque(self, data):
        if self.verifyTop:
            self.add(data, self._lenght)
        else:
            raise LinkedEmpty("Stack is full")
    
    @property
    def dequeque(self):
        if self.isEmpty:
            raise LinkedEmpty("Stack empty")
        else:
            return self.delete(0)