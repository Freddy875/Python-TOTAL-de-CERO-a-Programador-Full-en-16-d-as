# ------------------------------------------------------------
# Práctica Sets 4
# Elimina un elemento al azar del siguiente set utilizando
# métodos de sets.
# ------------------------------------------------------------

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}


# ------------------------------------------------------------
# Realizar el sorteo
# El método pop() elimina y devuelve un elemento del set.
# Como los sets no tienen un orden fijo, el elemento obtenido
# se utiliza como el ganador del sorteo.
# ------------------------------------------------------------

ganador = sorteo.pop()


# ------------------------------------------------------------
# Mostrar el ganador del sorteo
# Se utiliza un f-string para mostrar quién ganó el sorteo.
# ------------------------------------------------------------

print(f"Quien ganó el sorteo es: {ganador}")