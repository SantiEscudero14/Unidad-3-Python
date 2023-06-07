class Sabor():
    def __init__(self, idSabor, ingredientes, nombre):
        self.__idSabor=idSabor
        self.__ingredientes=ingredientes
        self.__nombre=nombre
        self.__cont=0
        
    def get_idSabor(self):
        return self.__idSabor
        
    def contador(self):
        self.__cont+=1
        