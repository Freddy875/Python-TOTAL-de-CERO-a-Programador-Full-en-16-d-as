# ------------------------------------------------------------
# Práctica Zip
# Utiliza zip() para combinar elementos de varias listas
# que se encuentran en la misma posición.
# También muestra qué ocurre cuando las listas tienen
# diferente cantidad de elementos.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Crea una lista de nombres y otra de edades.
# ------------------------------------------------------------

nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42]

# ------------------------------------------------------------
# zip() combina cada nombre con la edad que se encuentra
# en la misma posición.
# list() convierte el resultado en una lista de tuplas.
# ------------------------------------------------------------

combinados = list(zip(nombres, edades))

# Imprime: [('Ana', 65), ('Hugo', 29), ('Valeria', 42)]
print(combinados)


# ------------------------------------------------------------
# Si las listas tienen diferente cantidad de elementos,
# zip() se detiene cuando termina la lista más corta.
# Por lo tanto, los elementos sobrantes no se incluyen.
# ------------------------------------------------------------

nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42, 55]
ciudades = ["Lima", "Madrid", "Ciudad de México"]

# ------------------------------------------------------------
# Combina los nombres, edades y ciudades que se encuentran
# en la misma posición.
# ------------------------------------------------------------

combinados = list(zip(nombres, edades, ciudades))

# Imprime:
# [('Ana', 65, 'Lima'),
#  ('Hugo', 29, 'Madrid'),
#  ('Valeria', 42, 'Ciudad de México')]
print(combinados)


# ------------------------------------------------------------
# Recorre las tuplas de combinados.
# En cada vuelta se desempaquetan los tres valores:
# nombre, edad y ciudad.
# ------------------------------------------------------------

for nombre, edad, ciudad in combinados:

    # Imprime los datos de cada persona.
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")