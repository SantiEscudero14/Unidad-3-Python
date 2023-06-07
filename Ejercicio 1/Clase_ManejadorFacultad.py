import csv
from Clase_Facultad import Facultad
from Clase_Carrera import  Carrera

class ManejadorFacultad:
    def __init__(self):
        self.__lista=[]
    def Carga(self):
        archivo=open("Facultades.csv")
        reader=csv.reader(archivo,delimiter=",")
        codigo=int(-1)
        for fila in reader:
            c=int(fila[0])
            if (codigo!=c):
                codigo=c
                facu=Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(facu)
            else:
                carrera=Carrera(fila[1],fila[2],fila[3],fila[4],fila[5])
                
                self.__lista[codigo-1].AgregarCarrera(carrera)

    def BuscaFacultad(self,codigo):
        i=0
        band=False
        while(band==False)and(i< len(self.__lista)):
            if(self.__lista[i].getCodigo()==codigo):
                band=True
            else: i+=1
        if(band==False):
            i=-1
        return i
    def MostrarFacultad(self,num):
        print(f"Nombre de facultad: {self.__lista[num].getNombre()}")
        carreras=self.__lista[num].getCarreras()
        i=1
        for c in carreras:
            print(f"Carrera {i}:")
            i+=1
            print(f"Nombre {c.getNombre()}")
            print(f"Duracion: {c.getDuracion()}")
    def MostrarCarrera(self,i,codigo):
        print(f"Codigo: {self.__lista[i].getCodigo()},{codigo}")
        print(f"Nombre: {self.__lista[i].getNombre()}")
        print(f"Localidad: {self.__lista[i].getLocalidad()}")
    def BuscarCarrera(self,nombre):
        band=False
        i=0
        while (band==False)and(i<len(self.__lista)):
            j=0
            carreras=self.__lista[i].getCarreras()
            while(band==False)and(j<len(carreras)):
                if nombre==carreras[j].getNombre():
                    band=True
                else: 
                    j+=1
            if(band==False):
                i+=1
        if band==False:
            print("No se encontro la carrera")
        else:
            self.MostrarCarrera(i,carreras[j].getCodigo())
