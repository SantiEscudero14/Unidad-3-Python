from ClaseTallerCapacitacion import TallerCapacitacion
import csv
class ManejaTaller():
    def __init__(self):
        self.__ListaT=[]
        
    def cargar(self):
        band=False
        archivo=open("talleres.csv")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            if band == False:
                band=True
            else:
                Taller=TallerCapacitacion(int(fila[0]),fila[1],int(fila[2]),int(fila[3]))
                self.__ListaT.append(Taller)
    
    
        
        
        
    
    