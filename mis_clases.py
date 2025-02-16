class pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre #atributo privado para almacenar los nombres de las peliculas

    def __str__(self):
        return self.__nombre #devuelve el nombre de la pelicula como cadena de texto
    

class catalogopeliculas: #nombre del catalogo y ruta del archivo txt
    def __init__(self, nombre):
        self.nombre = nombre 
        self.ruta_archivo = f"{nombre}.txt"


    def agregar_peliculas(self, pelicula):
        with open(self.ruta_archivo, "a", encoding= "utf-8") as archivo:

            archivo.write(str(pelicula)+ "\n")

    def listar_peliculas(self):
        try:
          with open(self.ruta_archivo, "r", encoding= "utf-8") as archivo:
             peliculas = archivo.readlines()
          if peliculas:
                print("\nPeliculas en el catalogo: ")

                for pelicula in peliculas:
                   print(f"-{pelicula.strip()}")

          else:
                   print("\nEl catalogo esta vacio ❌")  #si el archivo existe pero esta vacio
        
        except FileNotFoundError:
          print("\nNo se ha ingresado ninguna pelicula aun ❌")

    def eliminar_catalogo(self):
       import os
       if os.path.exists(self.ruta_archivo):
          os.remove(self.ruta_archivo)
          print("\nEl catalogo se ha eliminado correctamente ❌")
       else:
          print("\nEl catalogo no existe ❌") #si YA se borró, o NUNCA existió