from Clase_ManejadorFacultad import ManejadorFacultad

if __name__=="__main__":
    MF=ManejadorFacultad()
    MF.Carga()
    opcion=-1
    while opcion!=0:
        print("-------MENU-----")
        print("1-Mostrar facultad")
        print("2-Mostrar carrera")
        opcion=int(input("Ingrese opcion: "))
        if(opcion!=0):
            if(opcion==1):
                codigo=int(input("Ingrese codigo de facultad: "))
                n=int(MF.BuscaFacultad(codigo))
                if(n==-1):
                    print("No se encontro la facultad")
                else:
                    MF.MostrarFacultad(n)
            elif opcion==2:
                nombre=input("Ingrese nombre de carrera: ")
                carrera=MF.BuscarCarrera(nombre)