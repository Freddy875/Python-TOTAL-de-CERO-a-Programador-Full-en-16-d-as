# ==================================================
# Práctica: Métodos Especiales 1
# Objetivo: Dada la clase Libro, implementar el método
# especial __str__ para que cada vez que se imprima el
# objeto, devuelva '"{titulo}", de {autor}' (el título
# debe estar encerrado entre comillas dobles).
# ==================================================

# --------------------------------------------------
# Definir la clase Libro
# Una clase es un molde que sirve para crear objetos;
# por convención, su nombre se escribe con la primera
# letra de cada palabra en mayúscula
# --------------------------------------------------
class Libro():
    """Clase que representa a un libro."""

    # ----------------------------------------------
    # Método constructor: __init__()
    # Se ejecuta al crear un objeto; recibe los valores
    # iniciales y los guarda como atributos de instancia:
    # titulo, autor y cantidad_paginas
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
    # Se ejecuta automáticamente al imprimir el objeto
    # con print(); devuelve el título entre comillas
    # dobles y el autor, por ejemplo:
    # "Don Quijote", de Miguel de Cervantes
    # ----------------------------------------------
    def __str__(self):
        """Devuelve la representación del libro en texto.

        Devuelve:
            Un texto con el formato '"titulo", de autor' (texto).
        """
        return f'"{self.titulo}", de {self.autor}'