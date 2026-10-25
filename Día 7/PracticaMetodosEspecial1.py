# ==================================================
# Práctica: Guardar libro en un archivo
# Objetivo: Pedir al usuario el título y el autor de un
# libro, crear una instancia de la clase Libro y guardar
# en un archivo de texto el libro con el formato
# '"{titulo}", de {autor}'.
# ==================================================

# --------------------------------------------------
# Definir la clase Libro
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula.
# Una instancia es el objeto en sí, creado a partir
# del molde; en esta clase, cada instancia es un libro
# con sus propios valores en los atributos.
# Atributos de clase: ninguno.
# Atributos de instancia: titulo, autor y
# cantidad_paginas.
# Instancias: se crea una más adelante, llamada libro
# --------------------------------------------------
class Libro():
    """Clase que representa a un libro."""

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta al crear una instancia; recibe los
    # valores iniciales y los guarda como atributos de
    # instancia, es decir, atributos que son propios de
    # cada libro: titulo, autor y cantidad_paginas
    # ----------------------------------------------
    def __init__(self, titulo, autor, cantidad_paginas):
        """Inicializa el libro.

        Parámetros:
            titulo: título del libro (texto).
            autor: autor del libro (texto).
            cantidad_paginas: número de páginas del libro (entero).
        """
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    # ----------------------------------------------
    # Método especial: __str__()
    # Se ejecuta automáticamente al imprimir una
    # instancia con print(); devuelve el título entre
    # comillas dobles y el autor, por ejemplo:
    # "Don Quijote", de Miguel de Cervantes
    # ----------------------------------------------
    def __str__(self):
        """Devuelve la representación del libro en texto.

        Devuelve:
            Un texto con el formato '"titulo", de autor' (texto).
        """
        return f'"{self.titulo}", de {self.autor}'


# --------------------------------------------------
# Pedir los datos del libro
# Se crean las variables titulo y autor, que guardan
# como texto lo que el usuario escribe con input()
# --------------------------------------------------
titulo = input("¿Cuál es el título del libro? ")
autor = input("¿Quién es el autor? ")

# --------------------------------------------------
# Crear la instancia de la clase Libro
# Se crea la variable libro, que es la instancia (un
# libro) con el título y el autor ingresados; como solo
# se piden esos dos datos, cantidad_paginas se
# inicializa en 0
# --------------------------------------------------
libro = Libro(titulo, autor, 0)

# --------------------------------------------------
# Guardar el libro en el archivo
# with abre el archivo libros.txt en modo agregar ("a")
# para conservar los libros guardados antes, y lo cierra
# automáticamente al terminar el bloque; write() escribe
# el libro (usando __str__) seguido de un salto de línea
# y archivo es la variable que representa el archivo abierto
# --------------------------------------------------
with open("libros.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{libro}\n")

# --------------------------------------------------
# Mostrar el mensaje de confirmación
# Se imprime el libro guardado; si el usuario escribe
# Don Quijote y Miguel de Cervantes, imprime:
# Libro guardado: "Don Quijote", de Miguel de Cervantes
# --------------------------------------------------
print(f"Libro guardado: {libro}")