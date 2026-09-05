# ------------------------------------------------------------
# Práctica Sets 1
# Une los siguientes sets en uno solo, llamado mi_set_3.
# ------------------------------------------------------------

mi_set_1 = {1, 2, "tres", "cuatro"}

mi_set_2 = {"tres", 4, 5}


# ------------------------------------------------------------
# Unir los dos sets
# El método union() combina los elementos de mi_set_1 y
# mi_set_2 en un nuevo set llamado mi_set_3.
# Los elementos repetidos, como "tres", aparecen una sola vez.
# ------------------------------------------------------------

mi_set_3 = mi_set_1.union(mi_set_2)


# ------------------------------------------------------------
# Mostrar el resultado
# Se imprime el nuevo set que contiene los elementos de ambos
# sets sin repetir los elementos duplicados.
# ------------------------------------------------------------

print(mi_set_3)