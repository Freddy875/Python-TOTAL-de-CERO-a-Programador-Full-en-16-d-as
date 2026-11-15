# ==================================================
# PRÁCTICA MÉTODOS ESPECIALES 1
# Objetivo: Implementar el método especial __str__
# en la clase Libro para que, al imprimir el objeto,
# devuelva '"{titulo}", de {autor}' con el título
# entre comillas dobles.
# ==================================================

# --------------------------------------------------
# CLASE LIBRO
# Representa un libro con su título y autor.
# --------------------------------------------------
class Libro():
    """Representa un libro."""

    # ------------------------------
    # Método: __init__
    # Atributos:
    # titulo: título del libro.
    # autor: autor del libro.
    # ------------------------------
    def __init__(self, titulo, autor):
        """Crea un libro con sus datos.

        Parámetros:
            titulo: título del libro.
            autor: autor del libro.
        Devuelve: nada, solo guarda los atributos.
        """
        self.titulo = titulo
        self.autor = autor

    # ------------------------------
    # Método: __str__
    # ------------------------------
    def __str__(self):
        """Define el texto que se muestra al imprimir el libro.

        Parámetros: ninguno.
        Devuelve: string con el formato "titulo", de autor.
        """
        return f'"{self.titulo}", de {self.autor}'

# --------------------------------------------------
# DATOS DEL USUARIO
# titulo: título que escribe el usuario.
# autor: autor que escribe el usuario.
# --------------------------------------------------
titulo = input("Escribe el título del libro: ")
autor = input("Escribe el autor del libro: ")

# --------------------------------------------------
# INSTANCIA E IMPRESIÓN DEL LIBRO
# mi_libro: instancia de Libro creada con los datos
# del usuario. Al imprimirla, Python llama a __str__.
# Resultado esperado: con Comer animales y Jonathan
# Safran Foer imprime
#   "Comer animales", de Jonathan Safran Foer
# --------------------------------------------------
mi_libro = Libro(titulo, autor)
print(mi_libro)