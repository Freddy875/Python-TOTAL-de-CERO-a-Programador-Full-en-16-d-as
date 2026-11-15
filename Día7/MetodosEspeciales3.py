# ==================================================
# PRÁCTICA MÉTODOS ESPECIALES 3
# Objetivo: Implementar el método especial __del__
# en la clase Libro para que, cada vez que el libro
# se elimine, se muestre en pantalla el mensaje
# "Libro eliminado".
# ==================================================

# --------------------------------------------------
# CLASE LIBRO
# Representa un libro con su título, autor y
# cantidad de páginas.
# --------------------------------------------------
class Libro():
    """Representa un libro."""

    # ------------------------------
    # Método: __init__
    # Atributos:
    # titulo: título del libro.
    # autor: autor del libro.
    # cantidad_paginas: número de páginas.
    # ------------------------------
    def __init__(self, titulo, autor, cantidad_paginas):
        """Crea un libro con sus datos.

        Parámetros:
            titulo: título del libro.
            autor: autor del libro.
            cantidad_paginas: número de páginas del libro.
        Devuelve: nada, solo guarda los atributos.
        """
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    # ------------------------------
    # Método: __del__
    # ------------------------------
    def __del__(self):
        """Avisa al usuario cuando el libro se elimina.

        Python lo llama al eliminar el objeto, por ejemplo
        con del o al terminar el programa.

        Parámetros: ninguno.
        Devuelve: nada, solo imprime "Libro eliminado".
        """
        print("Libro eliminado")