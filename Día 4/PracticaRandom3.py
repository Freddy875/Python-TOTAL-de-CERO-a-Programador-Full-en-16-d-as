# ------------------------------------------------------------
# Práctica Random 3
# Utiliza el método choice() de la librería random
# para seleccionar un nombre al azar de una lista.
# El nombre seleccionado se almacena en la variable sorteo.
# ------------------------------------------------------------

# Importamos la librería random para poder utilizar
# sus métodos relacionados con valores aleatorios.
import random

# ------------------------------------------------------------
# Lista de nombres entre los cuales se realizará el sorteo.
# ------------------------------------------------------------

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

# ------------------------------------------------------------
# choice() selecciona aleatoriamente un elemento de la lista.
# El nombre seleccionado se almacena en la variable sorteo.
# ------------------------------------------------------------

sorteo = random.choice(nombres)

# ------------------------------------------------------------
# Imprime el nombre seleccionado aleatoriamente.
# ------------------------------------------------------------

print(sorteo)