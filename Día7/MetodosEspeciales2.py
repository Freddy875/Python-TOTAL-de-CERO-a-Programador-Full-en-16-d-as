# ==================================================
# PRÁCTICA MÉTODOS ESPECIALES 2
# Objetivo: implementar el método especial __len__
# en la clase Libro para que, al ejecutar len() sobre
# el objeto, devuelva el número de páginas como
# número entero.
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
    # Método: __len__
    # ------------------------------
    def __len__(self):
        """Define lo que devuelve len() al usarse sobre el libro.

        Parámetros: ninguno.
        Devuelve: la cantidad de páginas como número entero.
        """
        return self.cantidad_paginas

# --------------------------------------------------
# DATOS DEL USUARIO
# titulo: título que escribe el usuario.
# autor: autor que escribe el usuario.
# cantidad_paginas: número de páginas que escribe el
# usuario, convertido a entero porque __len__ debe
# devolver un número entero.
# --------------------------------------------------
titulo = input("Escribe el título del libro: ")
autor = input("Escribe el autor del libro: ")
cantidad_paginas = int(input("Escribe la cantidad de páginas: "))

# --------------------------------------------------
# INSTANCIA E IMPRESIÓN DEL RESULTADO
# mi_libro: instancia de Libro creada con los datos
# del usuario.
# resultado: texto con el título, el autor y las
# páginas; len(mi_libro) llama a __len__.
# Resultado esperado: con Comer animales, Jonathan
# Safran Foer y 384 imprime
#   "Comer animales", de Jonathan Safran Foer, tiene 384 páginas
# --------------------------------------------------
mi_libro = Libro(titulo, autor, cantidad_paginas)
resultado = f'"{mi_libro.titulo}", de {mi_libro.autor}, tiene {len(mi_libro)} páginas'
print(resultado)

# --------------------------------------------------
# EXPORTACIÓN A ARCHIVO TXT
# El bloque with abre (o crea) el archivo libro.txt
# en modo escritura y lo cierra solo al terminar.
# Se guarda el mismo texto que se mostró en pantalla.
# Resultado esperado: libro.txt contiene
#   "Comer animales", de Jonathan Safran Foer, tiene 384 páginas
# --------------------------------------------------
with open("libro.txt", "w", encoding="utf-8") as archivo:
    # Escribe en el archivo el resultado del libro
    archivo.write(resultado)