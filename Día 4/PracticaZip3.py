# ------------------------------------------------------------
# Práctica Zip 3
# Crea un zip con las traducciones de los números del 1 al 5
# en español, portugués e inglés, manteniendo el mismo orden.
# Después convierte el objeto zip en una lista almacenada
# en la variable numeros.
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
# Imprime la lista con las traducciones agrupadas
# en tuplas de tres elementos.
# ------------------------------------------------------------

print(numeros)