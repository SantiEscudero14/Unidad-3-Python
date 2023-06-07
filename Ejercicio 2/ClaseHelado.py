class Helado():
    __gramos:float
    __precio:float
    def __init__(self, gramos, precio):
        self.__gramos=gramos
        self.__precio=precio
        self.__Sabor=[]
        
    def agregar_sabor(self, sabor, cant):
        for i in range(cant):
            self.__Sabor.append(sabor[i])
    