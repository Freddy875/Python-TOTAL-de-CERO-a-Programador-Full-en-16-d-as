# ------------------------------------------------------------
# Práctica Comprensión de Listas 1
# Crea una nueva lista llamada valores_cuadrado.
# La nueva lista contiene cada número de la lista valores
# elevado al cuadrado.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de valores originales que se utilizarán
# para crear la nueva lista.
# ------------------------------------------------------------

valores = [1, 2, 3, 4, 5, 6, 9.5]

# ------------------------------------------------------------
# Comprensión de listas
# Recorre cada valor de la lista valores y eleva cada uno
# al cuadrado utilizando ** 2.
# El resultado de cada operación se almacena en valores_cuadrado.
# ------------------------------------------------------------

valores_cuadrado = [numero**2 for numero in valores]

# ------------------------------------------------------------
# Imprime la nueva lista con todos los valores elevados
# al cuadrado.
# ------------------------------------------------------------

print(valores_cuadrado)