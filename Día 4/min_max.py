# ------------------------------------------------------------
# Función min()
# Obtiene el menor valor entre los números proporcionados.
# ------------------------------------------------------------

menor = min(58, 96, 72, 64, 35)

# Imprime: 35
print(menor)


# ------------------------------------------------------------
# Función max()
# Obtiene el mayor valor entre los números proporcionados.
# ------------------------------------------------------------

mayor = max(58, 96, 72, 64, 35)

# Imprime: 96
print(mayor)


# ------------------------------------------------------------
# min() y max() con una lista
# También podemos utilizar estas funciones directamente
# sobre una lista de números.
# ------------------------------------------------------------

lista_numerica = [58, 96, 72, 64, 35, 300]

# Imprime: 35
print(min(lista_numerica))

# ------------------------------------------------------------
# Muestra en una sola frase el menor y el mayor valor
# de la lista utilizando min() y max().
# ------------------------------------------------------------

print(f"El menor es {min(lista_numerica)} y el mayor es {max(lista_numerica)}")


# ------------------------------------------------------------
# min() con strings
# Con strings, min() busca el elemento que aparece primero
# según el orden de comparación de los caracteres.
# ------------------------------------------------------------

nombres = [
    "Marcos",
    "Laura",
    "Mónica",
    "Javier",
    "Celina",
    "Marta",
    "Darío",
    "Emiliano",
    "Melisa"
]

# Imprime: Celina
print(min(nombres))


# ------------------------------------------------------------
# min() con un string
# lower() convierte todos los caracteres a minúsculas
# antes de buscar el menor carácter.
# ------------------------------------------------------------

nombre = "Carlos"

# Imprime: a
print(min(nombre.lower()))


# ------------------------------------------------------------
# min() con diccionarios
# Al utilizar min() directamente sobre un diccionario,
# busca el menor elemento entre sus claves.
# ------------------------------------------------------------

diccionario = {"c1": 45, "c2": 11}

# Imprime: c1
print(min(diccionario))


# ------------------------------------------------------------
# min() sobre los valores de un diccionario
# values() obtiene los valores del diccionario.
# min() busca el menor valor dentro de ellos.
# ------------------------------------------------------------

# Imprime: 11
print(min(diccionario.values()))