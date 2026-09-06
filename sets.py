# ------------------------------------------------------------
# Crear un set a partir de una lista
# La función set() convierte los elementos de una lista en un
# set, una colección de elementos únicos y sin orden fijo.
# ------------------------------------------------------------

mi_set = set([1, 2, 3, 4, 5])

print(type(mi_set))  # Imprime: <class 'set'>

print(mi_set)  # Imprime los elementos del set en un orden que puede variar


# ------------------------------------------------------------
# Crear un set utilizando otro conjunto como argumento
# La función set() también puede utilizarse para crear un set
# a partir de una colección de elementos.
# ------------------------------------------------------------

mi_set2 = set({1, 2, 3, 4, 5})

print(type(mi_set2))  # Imprime: <class 'set'>

print(mi_set2)  # Imprime los elementos del set en un orden que puede variar


# ------------------------------------------------------------
# Crear un set a partir de una tupla
# La función set() convierte los elementos de la tupla en
# un set.
# ------------------------------------------------------------

mi_set3 = set((1, 2, 3, 4, 5))

print(type(mi_set3))  # Imprime: <class 'set'>

print(mi_set3)  # Imprime los elementos del set en un orden que puede variar


# ------------------------------------------------------------
# Crear un set utilizando llaves
# Esta es una forma directa de declarar un set en Python.
# ------------------------------------------------------------

mi_set4 = {1, 2, 3, 4, 5}

print(type(mi_set4))  # Imprime: <class 'set'>

print(mi_set4)  # Imprime los elementos del set en un orden que puede variar


# ------------------------------------------------------------
# Set con strings
# Un set puede contener elementos de tipo string.
# ------------------------------------------------------------

set_strings = {"Hola", "Mundo", "Python"}

print(type(set_strings))  # Imprime: <class 'set'>

print(set_strings)  # El orden de los elementos puede variar


# ------------------------------------------------------------
# Set de caracteres
# Un string puede separarse en caracteres individuales dentro
# de un set.
# ------------------------------------------------------------

set_chars = set({"a", "b", "c", "d", "e"})

print(type(set_chars))  # Imprime: <class 'set'>

print(set_chars)  # El orden de los caracteres puede variar


# ------------------------------------------------------------
# Set de valores booleanos
# Un set puede contener valores booleanos como True y False.
# ------------------------------------------------------------

set_bools = {True, False}

print(type(set_bools))  # Imprime: <class 'set'>

print(set_bools)  # El orden de los elementos puede variar


# ------------------------------------------------------------
# Set con múltiples tipos de datos
# Un set puede contener diferentes tipos de datos siempre que
# sus elementos puedan almacenarse dentro de un set.
# ------------------------------------------------------------

set_mixed = {1, "Hola", 3.14, True}

print(type(set_mixed))  # Imprime: <class 'set'>

print(set_mixed)  # El orden de los elementos puede variar


# ------------------------------------------------------------
# Set de tuplas
# Las tuplas pueden almacenarse dentro de un set porque son
# estructuras inmutables.
# ------------------------------------------------------------

set_tuples = {(1, 2), (3, 4), (5, 6)}

print(type(set_tuples))  # Imprime: <class 'set'>

print(set_tuples)  # El orden de las tuplas puede variar


# ------------------------------------------------------------
# Obtener la longitud de un set
# La función len() devuelve la cantidad de elementos que
# contiene el set.
# ------------------------------------------------------------

mi_set5 = {1, 2, 3, 4, 5}

print(len(mi_set5))  # Imprime: 5


# ------------------------------------------------------------
# Consultar si un elemento está en un set
# El operador in comprueba si un elemento se encuentra dentro
# del set y devuelve un valor booleano.
# ------------------------------------------------------------

mi_set6 = {1, 2, 3, 4, 5}

print(2 in mi_set6)  # Imprime: True

print(6 in mi_set6)  # Imprime: False


# ------------------------------------------------------------
# Unir dos sets
# El método union() combina los elementos de ambos sets en
# un nuevo set sin repetir elementos.
# ------------------------------------------------------------

set_7 = {1, 2, 3}

set_8 = {3, 4, 5}

union_sets = set_7.union(set_8)

print(union_sets)  # Imprime: {1, 2, 3, 4, 5} en un orden que puede variar


# ------------------------------------------------------------
# Agregar un elemento a un set
# El método add() agrega un nuevo elemento al set.
# ------------------------------------------------------------

set_9 = {1, 2, 3}

set_9.add(4)

print(set_9)  # Imprime los elementos incluyendo el número 4


# ------------------------------------------------------------
# Eliminar un elemento con remove()
# El método remove() elimina el elemento indicado del set.
# Produce un error si el elemento no existe.
# ------------------------------------------------------------

set_10 = {1, 2, 3, 4, 5}

set_10.remove(3)

print(set_10)  # Imprime el set sin el número 3


# ------------------------------------------------------------
# Eliminar un elemento con discard()
# El método discard() elimina el elemento indicado del set.
# Si el elemento no existe, no produce un error.
# ------------------------------------------------------------

set_11 = {1, 2, 3, 4, 5}

set_11.discard(3)

print(set_11)  # Imprime el set sin el número 3


# ------------------------------------------------------------
# Eliminar un elemento con pop()
# El método pop() elimina y devuelve un elemento del set.
# Como los sets no tienen un orden fijo, no se puede elegir
# el elemento mediante un índice.
# ------------------------------------------------------------

set_12 = {1, 2, 3, 4, 5}

set_12.pop()

print(set_12)  # Imprime el set después de eliminar un elemento


# ------------------------------------------------------------
# Utilizar pop() para realizar un sorteo
# El elemento eliminado por pop() se guarda en la variable
# sorteo y posteriormente se muestra en pantalla.
# ------------------------------------------------------------

set_13 = {1, 2, 3, 4, 5}

sorteo = set_13.pop()

print(sorteo)  # Imprime el elemento obtenido del set


# ------------------------------------------------------------
# Limpiar un set
# El método clear() elimina todos los elementos que contiene
# el set.
# ------------------------------------------------------------

set_14 = {1, 2, 3, 4, 5}

print(set_14)  # Imprime el set antes de limpiarlo

set_14.clear()

print(set_14)  # Imprime: set()
