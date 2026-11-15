# ------------------------------------------------------------
# Práctica Rango 1
#
# Crea una lista formada por todos los números desde el 2500
# hasta el 2585, incluyendo ambos valores.
#
# La lista debe almacenarse en la variable mi_lista.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Crear la lista de números
#
# range() genera los números desde 2500 hasta antes de 2586.
#
# Como el segundo valor de range() no se incluye, se utiliza
# 2586 para que el último número generado sea 2585.
#
# list() convierte el rango generado en una lista.
# ------------------------------------------------------------

mi_lista = list(range(2500, 2586))


# ------------------------------------------------------------
# Imprimir la lista
#
# Se muestra el contenido de mi_lista para comprobar que
# contiene todos los números desde 2500 hasta 2585.
# ------------------------------------------------------------

print(mi_lista)