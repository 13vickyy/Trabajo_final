from mis_clases import pelicula, catalogopeliculas

print("\nBienvenido al catalogo de peliculas")

def menu(): #funcion principal
    nombre_catalogo = input("Ingrese un nombre de catalogo: ")
    catalogo = catalogopeliculas(nombre_catalogo)

    opciones= {
        1: "Agregar peliculas",
        2: "Listar peliculas",
        3: "Eliminar catalogo de peliculas",
        4: "Salir"
    }

    while True:
        print("\nMenu de opciones: ")
        for clave, valor in opciones.items():
            print(f"{clave}.{valor}")

        opcion= input("\nSeleccione una opcion: ")
        
        try:
            opcion_numerica= int(opcion) #conversion opcion a entero

        except ValueError:
            print("\nOpcion invalida ❌, ingrese un numero valido")

            continue
        
        if opcion_numerica == 1:
            nombre_pelicula = input("\nIngrese el nombre de la pelicula: ")
            pelicula_nueva = pelicula(nombre_pelicula)
            catalogo.agregar_peliculas(pelicula_nueva)
            print(f"\nPelicula {nombre_pelicula} ha sido ingresada correctamente ✔️")

        elif opcion_numerica == 2: 
           catalogo.listar_peliculas() 

        elif opcion_numerica == 3:
            catalogo.eliminar_catalogo()

        elif opcion_numerica == 4:
            print("\nSaliendo del programa")
            break

        else:
            print("\nOpcion invalida ❌, ingrese la opcion nuevamente")

#Llamo funcion principal
menu()

