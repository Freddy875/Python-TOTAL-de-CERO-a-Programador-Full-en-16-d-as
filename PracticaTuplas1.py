# ------------------------------------------------------------
# Tupla con números repetidos
# La tupla contiene varios números, incluyendo el número 2
# en diferentes posiciones.
# ------------------------------------------------------------

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)


# ------------------------------------------------------------
# Método count()
# count() cuenta cuántas veces aparece el número 2 dentro
# de la tupla y guarda el resultado en la variable
# cantidad_dos.
# ------------------------------------------------------------

cantidad_dos = mi_tupla.count(2)


# ------------------------------------------------------------
# Mostrar el resultado
# Se imprime la cantidad de veces que aparece el número 2.
# ------------------------------------------------------------

print(cantidad_dos)  # Imprime: 6