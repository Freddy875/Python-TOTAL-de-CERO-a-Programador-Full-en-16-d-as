# ------------------------------------------------------------
# Práctica Comprensión de Listas 4
# Utiliza la función pow() del módulo math para elevar al
# cuadrado cada uno de los valores de una lista.
# Los resultados se almacenan en una nueva lista.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Importamos el módulo math para utilizar sus funciones
# matemáticas.
# ------------------------------------------------------------

import math

# ------------------------------------------------------------
# Lista de valores originales que se utilizarán
# para realizar las operaciones.
# ------------------------------------------------------------

valores = [1, 2, 3, 4, 5, 6, 9.5]

# ------------------------------------------------------------
# Comprensión de listas
# Recorre cada valor de la lista y utiliza math.pow()
# para elevarlo al cuadrado.
# math.pow(x, 2) significa elevar x a la potencia 2.
# ------------------------------------------------------------

valores_cuadrado = [math.pow(numero, 2) for numero in valores]

# ------------------------------------------------------------
# Imprime la nueva lista con los valores elevados
# al cuadrado.
# ------------------------------------------------------------

print(valores_cuadrado)