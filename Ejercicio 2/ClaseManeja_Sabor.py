from ClaseSabor import Sabor
import csv

class ManejaSabor():
    def __init__(self):
        self.__ListaS=[]
        
    def carga(self):
        band=False
        archivo=open("Sabores.csv")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            if band==False:
                band=True
            else:
                sabor=Sabor(int(fila[0]),fila[1], fila[2])
                self.__ListaS.append(sabor)
    
    def busca_sabor(self, sabor):
        band=False
        i=0
        while band==False and i<len(self.__ListaS):
            if sabor == self.__ListaS[i].get_idSabor():
                band=True
            else: i+=1
        if band==True:
            return self.__ListaS[i]
        else: print("No se encontro el sabor buscado")
        
    def contarSabor(self, sabor):
        i=0
        while i<len(self.__ListaS):
            if sabor == self.__ListaS[i].get_idSabor():
                self.__ListaS[i].contador()
            
        

    