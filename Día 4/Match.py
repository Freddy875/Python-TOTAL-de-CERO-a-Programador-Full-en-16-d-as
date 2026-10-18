# ------------------------------------------------------------
# Hacer coincidir un número de serie con una marca
#
# Se almacena una serie de teléfono en la variable serie.
# match permite identificar qué marca corresponde a esa serie.
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
# match compara el valor almacenado en serie con cada case.
# Cuando encuentra una coincidencia, ejecuta el código
# correspondiente.
#
# case _ funciona como una opción general cuando ningún
# caso anterior coincide.
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
# Se almacenan el nombre, la edad y la ocupación del cliente.
# ------------------------------------------------------------

cliente = {
    "nombre": "Juan",
    "edad": 30,
    "ocupación": "Instructor"
}


# ------------------------------------------------------------
# Crear un diccionario con información de una película
#
# Se almacena el título y una ficha técnica con información
# sobre la película.
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
# Crear un diccionario con información de una segunda película
#
# Se almacena el título y una ficha técnica con información
# sobre Jurassic Park.
# ------------------------------------------------------------

pelicula2 = {
    "titulo": "Jurassic Park",
    "ficha_técnica": {
        "protagonista": "Sam Neill",
        "director": "Steven Spielberg",
        "año": 1993,
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
# Crear un diccionario con información de un segundo libro
#
# Se almacenan el título y el autor del libro.
# ------------------------------------------------------------

libro2 = {
    "titulo": "Los 7 hábitos de la gente altamente efectiva",
    "autor": "Stephen Covey"
}


# ------------------------------------------------------------
# Crear una lista con todos los elementos
#
# Se agrupan el cliente, las películas y los libros dentro
# de una misma lista para poder recorrerlos posteriormente.
# ------------------------------------------------------------

elemento = [cliente, pelicula, pelicula2, libro, libro2]


# ------------------------------------------------------------
# Recorrer los elementos de la lista
#
# for recorre cada elemento de la lista.
# match analiza la estructura de cada diccionario para
# determinar si corresponde a un cliente, una película
# o un libro.
# ------------------------------------------------------------

for e in elemento:
    match e:

        # ----------------------------------------------------
        # Identificar un cliente
        #
        # Busca un diccionario que contenga las claves nombre,
        # edad y ocupación.
        # ----------------------------------------------------

        case {"nombre": nombre, "edad": edad, "ocupación": ocupacion}:
            print(f"Cliente: {nombre}, Edad: {edad}, Ocupación: {ocupacion}")

        # ----------------------------------------------------
        # Identificar una película
        #
        # Busca un diccionario que contenga un título y una
        # ficha técnica con protagonista, director, año y género.
        # ----------------------------------------------------

        case {"titulo": titulo, "ficha_técnica": {"protagonista": protagonista, "director": director, "año": año, "género": genero}}:
            print(f"Película: {titulo}, Protagonista: {protagonista}, Director: {director}, Año: {año}, Género: {genero}")

        # ----------------------------------------------------
        # Identificar un libro
        #
        # Busca un diccionario que contenga las claves titulo
        # y autor.
        # ----------------------------------------------------

        case {"titulo": titulo, "autor": autor}:
            print(f"Libro: {titulo}, Autor: {autor}")

        # ----------------------------------------------------
        # Caso que no coincide
        #
        # El guion bajo (_) funciona como un caso general
        # cuando ningún case anterior coincide.
        # ----------------------------------------------------

        case _:
            print("Elemento desconocido")