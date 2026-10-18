# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (*args) 1
# Crear una función que reciba una cantidad indeterminada
# de números y retorne la suma de sus valores al cuadrado.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para sumar los cuadrados
# *numeros permite recibir una cantidad variable de argumentos.
# La expresión num ** 2 eleva cada número al cuadrado.
# sum() suma todos los cuadrados calculados.
# ------------------------------------------------------------
def suma_cuadrados(*numeros):
    return sum(num ** 2 for num in numeros)


# ------------------------------------------------------------
# No se invoca la función, según la consigna.
# ------------------------------------------------------------