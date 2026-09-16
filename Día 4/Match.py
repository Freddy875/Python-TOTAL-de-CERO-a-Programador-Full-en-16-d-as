# ------------------------------------------------------------
# Hacer coincidir una serie con una marca
#
# Se almacena una serie de teléfono en la variable serie.
# Después se utiliza match para identificar qué marca
# corresponde a esa serie.
# ------------------------------------------------------------

serie = "N-02"


# ------------------------------------------------------------
# Alternativa utilizando if, elif y else
#
# Esta estructura comprueba el valor de serie mediante
# diferentes condiciones.
#
# Está dentro de un comentario multilínea, por lo que no
# se ejecuta.
# ------------------------------------------------------------

"""
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Apple")
elif serie == "N-03":
    print("Xiaomi")
elif serie == "N-04":
    print("Motorola")
elif serie == "N-05":
    print("Huawei")
elif serie == "N-06":
    print("LG")
elif serie == "N-07":
    print("Sony")
elif serie == "N-08":
    print("Nokia")
else:
    print("Serie no reconocida")
"""


# ------------------------------------------------------------
# Utilizar match y case
#
# match compara el valor almacenado en serie con los
# diferentes patrones indicados en cada case.
#
# Cuando encuentra una coincidencia, ejecuta el código
# correspondiente y deja de comprobar los demás casos.
# ------------------------------------------------------------

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Apple")
    case "N-03":
        print("Xiaomi")
    case "N-04":
        print("Motorola")
    case "N-05":
        print("Huawei")
    case "N-06":
        print("LG")
    case "N-07":
        print("Sony")
    case "N-08":
        print("Nokia")
    case _:
        print("Serie no reconocida")


# ------------------------------------------------------------
# Crear un diccionario con información de un cliente
#
# Se crea un diccionario que contiene el nombre, edad
# y ocupación del cliente.
# ------------------------------------------------------------

cliente = {
    "nombre": "Juan",
    "edad": 30,
    "ocupación": "Instructor"
}


# ------------------------------------------------------------
# Crear un diccionario con información de una película
#
# El diccionario contiene el título de la película y otro
# diccionario llamado ficha_técnica con información adicional.
# ------------------------------------------------------------

pelicula = {
    "titulo": "Matrix",
    "ficha_técnica": {
        "protagonista": "Keanu Reeves",
        "director": "Lana y Lilly Wachowski",
        "año": 1999,
        "género": "Ciencia ficción"
    }
}


# ------------------------------------------------------------
# Crear un diccionario con información de un libro
#
# Se almacenan el título y el autor del libro.
# ------------------------------------------------------------

libro = {
    "titulo": "1984",
    "autor": "George Orwell"
}


# ------------------------------------------------------------
# Crear una lista con los elementos
#
# Se agrupan los diccionarios de cliente, película y libro
# dentro de una misma lista.
# ------------------------------------------------------------

elemento = [cliente, pelicula, libro]


# ------------------------------------------------------------
# Recorrer los elementos de la lista
#
# for recorre cada diccionario almacenado en elemento.
# match permite identificar qué tipo de información contiene
# cada diccionario mediante su estructura y sus claves.
# ------------------------------------------------------------

for e in elemento:
    match e:

        # ----------------------------------------------------
        # Identificar un cliente
        #
        # Se busca un diccionario que contenga las claves
        # nombre, edad y ocupación.
        #
        # Los valores encontrados se almacenan en las variables
        # nombre, edad y ocupacion.
        # ----------------------------------------------------

        case {"nombre": nombre, "edad": edad, "ocupación": ocupacion}:
            print(f"Cliente: {nombre}, Edad: {edad}, Ocupación: {ocupacion}")

        # ----------------------------------------------------
        # Identificar una película
        #
        # Se busca un diccionario que contenga titulo y
        # ficha_técnica, incluyendo las claves de la ficha:
        # protagonista, director, año y género.
        # ----------------------------------------------------

        case {"titulo": titulo, "ficha_técnica": {"protagonista": protagonista, "director": director, "año": año, "género": genero}}:
            print(f"Película: {titulo}, Protagonista: {protagonista}, Director: {director}, Año: {año}, Género: {genero}")

        # ----------------------------------------------------
        # Identificar un libro
        #
        # Se busca un diccionario que contenga las claves
        # titulo y autor.
        # ----------------------------------------------------

        case {"titulo": titulo, "autor": autor}:
            print(f"Libro: {titulo}, Autor: {autor}")

        # ----------------------------------------------------
        # Caso que no coincide
        #
        # El guion bajo (_) funciona como un caso general
        # que se ejecuta cuando ningún case anterior coincide.
        # ----------------------------------------------------

        case _:
            print("Elemento desconocido")