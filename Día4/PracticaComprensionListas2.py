# ------------------------------------------------------------
# Práctica Comprensión de Listas 2
# Crea una nueva lista llamada valores_pares.
# La nueva lista contiene únicamente los números pares
# de la lista valores.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de valores originales que se utilizarán
# para encontrar los números pares.
# ------------------------------------------------------------

valores = [1, 2, 3, 4, 5, 6, 9.5]

# ------------------------------------------------------------
# Comprensión de listas
# Recorre cada valor de la lista.
# isinstance(x, int) verifica que el valor sea un entero.
# x % 2 == 0 verifica que el número sea divisible entre 2
# sin dejar residuo.
# Solo los valores que cumplen ambas condiciones
# se almacenan en valores_pares.
# ------------------------------------------------------------

valores_pares = [numero for numero in valores if isinstance(numero, int) and numero % 2 == 0]

# ------------------------------------------------------------
# Imprime la nueva lista que contiene únicamente
# los números pares.
# ------------------------------------------------------------

print(valores_pares)