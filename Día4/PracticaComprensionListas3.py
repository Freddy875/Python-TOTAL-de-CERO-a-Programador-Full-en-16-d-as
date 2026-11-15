# ------------------------------------------------------------
# Práctica Comprensión de Listas 3
# Convierte una lista de temperaturas expresadas en Fahrenheit
# a una nueva lista de temperaturas expresadas en Celsius.
# Utiliza una comprensión de listas para realizar la conversión.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de temperaturas expresadas en grados Fahrenheit.
# ------------------------------------------------------------

temperatura_fahrenheit = [32, 212, 275]

# ------------------------------------------------------------
# Comprensión de listas
# Recorre cada temperatura de la lista y aplica la fórmula
# para convertir grados Fahrenheit a grados Celsius:
#
# °C = (°F - 32) * (5 / 9)
#
# Cada resultado se almacena en la nueva lista grados_celsius.
# ------------------------------------------------------------

grados_celsius = [(temperatura - 32) * (5/9) for temperatura in temperatura_fahrenheit]

# ------------------------------------------------------------
# Imprime la nueva lista con las temperaturas convertidas
# de Fahrenheit a Celsius.
# ------------------------------------------------------------

print(grados_celsius)