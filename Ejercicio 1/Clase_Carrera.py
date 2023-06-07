class Carrera:
    def __init__(self,codigo,nombre,fecha,duracion,titulo):
        self.__codigo=int(codigo)
        self.__nombre=nombre
        self.__fecha=fecha
        self.__duracion=duracion
        self.__titulo=titulo
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getCodigo(self):
        return self.__codigo