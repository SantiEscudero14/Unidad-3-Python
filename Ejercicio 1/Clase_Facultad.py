from Clase_Carrera import Carrera
class Facultad:
    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo=int(codigo)
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carreras=[]
    def AgregarCarrera(self,carrera):
        self.__carreras.append(carrera)   
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getCarreras(self):
        return self.__carreras
    def getLocalidad(self):
        return self.__localidad