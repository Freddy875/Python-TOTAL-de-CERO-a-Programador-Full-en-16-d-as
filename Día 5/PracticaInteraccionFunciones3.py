# ------------------------------------------------------------
# Práctica sobre Interacción entre Funciones 3
# Crear una función que lance una moneda al azar y otra que
# utilice el resultado para decidir si la lista se conserva
# o se devuelve vacía.
# ------------------------------------------------------------

import random  # Importa la biblioteca para generar resultados aleatorios


# ------------------------------------------------------------
# Función para lanzar la moneda
# Elige aleatoriamente entre "Cara" y "Cruz" y devuelve
# el resultado sin recibir argumentos.
# ------------------------------------------------------------
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])


# ------------------------------------------------------------
# Función para probar suerte con la lista
# Recibe el resultado de la moneda y una lista de números.
# Si sale "Cara", devuelve una lista vacía.
# Si sale "Cruz", devuelve la lista original sin modificarla.
# ------------------------------------------------------------
def probar_suerte(resultado_moneda, lista):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista


# ------------------------------------------------------------
# Crear la lista de números que se utilizará como argumento
# al llamar a la función probar_suerte().
# ------------------------------------------------------------
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ------------------------------------------------------------
# No se invocan las funciones, según la consigna.
# ------------------------------------------------------------
