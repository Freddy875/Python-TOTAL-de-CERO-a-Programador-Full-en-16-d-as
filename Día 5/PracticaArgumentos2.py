# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (*args) 2
# Crear una función que reciba una cantidad indeterminada
# de números y devuelva la suma de sus valores absolutos.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para sumar los valores absolutos
# *numeros permite recibir una cantidad variable de argumentos.
# abs() obtiene el valor absoluto de cada número, eliminando
# su signo negativo cuando lo tiene.
# sum() suma todos los valores absolutos obtenidos.
# ------------------------------------------------------------
def suma_absolutos(*numeros):
    return sum(abs(numero) for numero in numeros)


# ------------------------------------------------------------
# No se invoca la función, según la consigna.
# ------------------------------------------------------------