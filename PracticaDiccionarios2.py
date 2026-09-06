# ------------------------------------------------------------
# Acceder a un elemento dentro de estructuras anidadas
# Primero se utiliza la clave "puntos" para acceder al
# diccionario interno. Después, la clave "points2" permite
# acceder a la lista.
# ------------------------------------------------------------

mi_dict = {
    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {"points1": 9, "points2": [10, 300, 15]}
}


# ------------------------------------------------------------
# Obtener el segundo elemento de la lista
# El índice 1 corresponde al segundo elemento, ya que Python
# comienza a contar las posiciones desde el índice 0.
# ------------------------------------------------------------

segundo_item = mi_dict["puntos"]["points2"][1]


# ------------------------------------------------------------
# Mostrar el valor obtenido
# Se imprime el elemento que ocupa la segunda posición de
# la lista points2.
# ------------------------------------------------------------

print(segundo_item)