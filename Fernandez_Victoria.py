from clases import pelicula, catalogopeliculas

print("\nBienvenido al catalogo de peliculas")

def menu(): #funcion principal
    nombre_catalogo = input("Ingrese un nombre de catalogo: ")
    catalogo = catalogopeliculas(nombre_catalogo)

    while True:
        print("\nMenu de opciones: ")
        print("1. Agregar peliculas")
        print("2. Listar peliculas")
        print("3. Eliminar catalogo de peliculas")
        print("4. Salir")

        opcion= input("\nSeleccione una opcion: ")

        if opcion == 1:
            nombre_pelicula = input("\nIngrese el nombre de la pelicula: ")
            pelicula = pelicula(nombre_pelicula)
            catalogo.agregar_peliculas(pelicula)

        elif opcion == 2: 
            catalogo.listar_peliculas() #continuar con codigo class

        elif opcion == 3:
            catalogo.eliminar_peliculas() #continuar con codigo class

        elif opcion == 4:
            print("\nSaliendo del programa")
            break

        else:
            print("\nOpcion invalida, ingrese la opcion nuevamente")

            