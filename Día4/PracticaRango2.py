# ------------------------------------------------------------
# Práctica Rango 2
#
# Utilizando la función range(), crea en una única línea de
# código una lista formada por todos los números múltiplos de 3
# desde el 3 hasta el 300, incluyendo ambos valores.
#
# La lista debe almacenarse en la variable mi_lista.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Crear la lista de múltiplos de 3
#
# range() comienza en 3, termina antes de 301 y avanza
# de 3 en 3.
#
# El tercer argumento, 3, indica el paso del rango.
# list() convierte el rango generado en una lista.
# ------------------------------------------------------------

mi_lista = list(range(3, 301, 3))


# ------------------------------------------------------------
# Imprimir la lista
#
# Se muestra el contenido de mi_lista para comprobar que
# contiene los múltiplos de 3 desde 3 hasta 300.
# ------------------------------------------------------------

print(mi_lista)