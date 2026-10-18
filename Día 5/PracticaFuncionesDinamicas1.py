# ------------------------------------------------------------
# Práctica Funciones Dinámicas 1
# Crear una función llamada todos_positivos que reciba una
# lista de números como parámetro.
# La función debe devolver True si todos los valores de la
# lista son positivos y False si al menos uno es negativo.
# También se debe crear una lista llamada lista_numeros con
# valores positivos y negativos.
# No se debe invocar la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función que verifica si todos los números son
# positivos.
# all() devuelve True si todos los valores cumplen la condición.
# num > 0 comprueba que cada número sea mayor que cero.
# ------------------------------------------------------------

def todos_positivos(lista):
    return all(num > 0 for num in lista)  # all() devuelve True si todos los valores cumplen la condición


# ------------------------------------------------------------
# Crear una lista con valores positivos y negativos
# La lista contiene varios números positivos y un número
# negativo para poder comprobar posteriormente la función.
# ------------------------------------------------------------

lista_numeros = [10, 5, 8, -3, 7, 12]  # Contiene un número negativo