# ------------------------------------------------------------
# Práctica Sets 2
# Elimina un elemento al azar del siguiente set utilizando
# métodos de sets.
# ------------------------------------------------------------

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}


# ------------------------------------------------------------
# Eliminar un elemento del set
# El método pop() elimina y devuelve un elemento del set.
# Como los sets no tienen un orden fijo, no se puede saber
# con anticipación qué elemento será eliminado.
# ------------------------------------------------------------

eliminado = sorteo.pop()


# ------------------------------------------------------------
# Mostrar el elemento eliminado
# Se utiliza un f-string para mostrar el elemento que fue
# eliminado del set y almacenado en la variable eliminado.
# ------------------------------------------------------------

print(f"Elemento eliminado: {eliminado}")


# ------------------------------------------------------------
# Mostrar el set actualizado
# Se imprime el set después de eliminar uno de sus elementos.
# El orden de los elementos puede variar.
# ------------------------------------------------------------

print(f"Set actualizado: {sorteo}")