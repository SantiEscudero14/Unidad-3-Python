from ClaseManeja_Helados import ManejaHelados
from ClaseManeja_Sabor import ManejaSabor
from clase_menu import Menu


if __name__ == "__main__":
    ManejaH= ManejaHelados()
    ManejaS= ManejaSabor()
    ManejaS.carga()
    
    opciones = ["Registrar un helado vendido","Mostrar el nombre de los 5 sabores de helado más pedidos.","Ingresar un número de sabor y estimar el total de gramos vendidos"," Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.", "Determinar el importe total recaudado por la Heladería, por cada tipo de helado."]
    menu = Menu(4)
    menu.IngresaOpcion(opciones)
    
    menu.Muestra()
    op = int(input("Ingrese opcion: "))
    
    while op != menu.getCantidad() + 1:
        if op == 1:
            sabores=[]
            idsabor=int(input("ingrese id de sabor, 0 para finalizar"))
            while idsabor != 0:
                sabor=ManejaSabor.busca_sabor(idsabor)
                ManejaSabor.contarSabor(idsabor)
                sabores.append(sabor)
                gramos=int("ingrese cantiddad de gramos")
                precio=float("ingrese precio de helado")
                ManejaHelados.agregar_helado(gramos, precio, sabores)
                print("helado registrado exitosamente")
                idsabor=int(input("ingrese id de sabor, 0 para finalizar"))
                
                
            
        elif op == 2:
             print("hola")
             
             
             
        elif op == 3:
             print("hola")
        elif op == 4:
             print("hola")
        elif op == 5:
            print("")
        else:
            print("Ingreso opcion incorrecta")
        menu.Muestra()
        op = int(input("Ingrese opcion: "))