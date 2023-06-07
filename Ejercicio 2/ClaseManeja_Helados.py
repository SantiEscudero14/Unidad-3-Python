from ClaseHelado import Helado
class ManejaHelados():
    def __init__(self):
        self.__Lista=[]
        
    def agregar_helado(self, gramos, precio, sabor):
        helado=Helado(precio,gramos)
        helado.agregar_sabor(sabor,len(sabor))
        self.__Lista.append(helado)
        