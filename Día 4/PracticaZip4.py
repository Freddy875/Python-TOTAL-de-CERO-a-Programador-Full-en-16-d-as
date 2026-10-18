# ------------------------------------------------------------
# Práctica Zip 4
# Recorre la lista de traducciones creada con zip()
# y muestra los números en español, portugués e inglés.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Listas con las traducciones de los números.
# Cada posición contiene el mismo número en los tres idiomas.
# ------------------------------------------------------------

espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

# ------------------------------------------------------------
# zip() combina los elementos que se encuentran
# en la misma posición de las tres listas.
# list() convierte el objeto zip en una lista de tuplas.
# ------------------------------------------------------------

numeros = list(zip(espanol, portugues, ingles))

# ------------------------------------------------------------
# Imprime la lista de traducciones agrupadas en tuplas.
# ------------------------------------------------------------

print(numeros)

# ------------------------------------------------------------
# Recorre cada tupla de la lista numeros.
# En cada vuelta se desempaquetan los tres valores:
# español, portugués e inglés.
# ------------------------------------------------------------

for espanol, portugues, ingles in numeros:

    # --------------------------------------------------------
    # Imprime las traducciones de cada número.
    # --------------------------------------------------------

    print(
        f"Español: {espanol} | "
        f"Portugués: {portugues} | "
        f"Inglés: {ingles}"
    )