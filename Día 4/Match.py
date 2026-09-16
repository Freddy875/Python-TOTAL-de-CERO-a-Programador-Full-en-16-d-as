### Hacer coicidir un número con serie con una marca

serie = "N-02"

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


cliente = {
    "nombre": "Juan",
    "edad": 30,
    "ocupación": "Instructor"
}

pelicula = {
    "titulo": "Matrix",
    "ficha_técnica": {
        "protagonista": "Keanu Reeves",
        "director": "Lana y Lilly Wachowski",
        "año": 1999,
        "género": "Ciencia ficción"
    }
}

libro = {
    "titulo": "1984",
    "autor": "George Orwell"
}

elemento = [cliente, pelicula, libro]

for e in elemento:
    match e:
        case {"nombre": nombre, "edad": edad, "ocupación": ocupacion}:
            print(f"Cliente: {nombre}, Edad: {edad}, Ocupación: {ocupacion}")
        case {"titulo": titulo, "ficha_técnica": {"protagonista": protagonista, "director": director, "año": año, "género": genero}}:
            print(f"Película: {titulo}, Protagonista: {protagonista}, Director: {director}, Año: {año}, Género: {genero}")
        case {"titulo": titulo, "autor": autor}:
            print(f"Libro: {titulo}, Autor: {autor}")
        case _:
            print("Elemento desconocido")

