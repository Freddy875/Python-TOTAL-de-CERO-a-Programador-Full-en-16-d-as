# ==================================================
# Práctica: Métodos Especiales 2
# Objetivo: Dada la clase Libro, implementar el método
# especial __len__ para que cada vez que se ejecute la
# función len() sobre el objeto, devuelva el número de
# páginas como número entero.
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
# Instancias: en este código no se crea ninguna; cada
# vez que se llame a Libro(titulo, autor,
# cantidad_paginas) se creará una instancia nueva
# (un libro)
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
    # Método especial: __len__()
    # Se ejecuta automáticamente al usar la función
    # len() sobre una instancia; devuelve el valor del
    # atributo cantidad_paginas, es decir, el número de
    # páginas del libro como número entero
    # ----------------------------------------------
    def __len__(self):
        """Devuelve el número de páginas del libro.

        Devuelve:
            El número de páginas del libro (entero).
        """
        return self.cantidad_paginas