# ------------------------------------------------------------
# Forma tradicional
# Recorre la lista utilizando una variable para controlar
# manualmente el índice de cada elemento.
# ------------------------------------------------------------

mi_lista = ["a", "b", "c"]

# ------------------------------------------------------------
# El índice comienza en 0 porque las listas en Python
# comienzan a contar sus posiciones desde 0.
# ------------------------------------------------------------

indice = 0

# ------------------------------------------------------------
# Recorre cada elemento de la lista.
# Imprime el índice junto con el elemento correspondiente.
# Después aumenta el índice en 1 para pasar a la siguiente posición.
# ------------------------------------------------------------

for item in mi_lista:
    print(indice, item)
    indice += 1


# ------------------------------------------------------------
# Forma con enumerate()
# Permite obtener automáticamente el índice y el elemento
# de cada posición de la lista.
# ------------------------------------------------------------

for indice, item in enumerate(mi_lista):
    print(indice, item)


print("\n")


# ------------------------------------------------------------
# Imprimir un enumerate() de un rango
# enumerate() también puede utilizarse con un range().
# En este caso, recorre los números del 50 al 54.
# ------------------------------------------------------------

for indice, item in enumerate(range(50, 55)):
    print(item, indice)


print("\n")


# ------------------------------------------------------------
# Usar enumerate() fuera de bucles
# list() convierte el objeto enumerate en una lista.
# Cada elemento queda formado por una pareja:
# (índice, elemento)
# ------------------------------------------------------------

mis_elementos = list(enumerate(mi_lista))
print(mis_elementos)


# ------------------------------------------------------------
# Acceder solo a un elemento
# [1] accede al segundo elemento de la lista,
# porque los índices comienzan desde 0.
# ------------------------------------------------------------

mis_elementos = list(enumerate(mi_lista))
print(mis_elementos[1])


# ------------------------------------------------------------
# Acceder a una coordenada
# El primer [1] selecciona el segundo elemento de la lista.
# El segundo [0] selecciona el primer valor de esa pareja:
# el índice.
# ------------------------------------------------------------

mis_elementos = list(enumerate(mi_lista))
print(mis_elementos[1][0])