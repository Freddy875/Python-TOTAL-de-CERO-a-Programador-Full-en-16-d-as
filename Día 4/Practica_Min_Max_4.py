# ------------------------------------------------------------
# Práctica Min y Max 4
# Obtiene el valor máximo entre los valores de una lista
# y lo almacena en una variable llamada valor_maximo.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de números con diversas operaciones matemáticas.
# ------------------------------------------------------------

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

# ------------------------------------------------------------
# Obtiene el valor máximo de la lista.
# ------------------------------------------------------------

valor_maximo = max(lista_numeros)

# ------------------------------------------------------------
# Recorre la lista e imprime cada uno de sus números.
# ------------------------------------------------------------

for numero in lista_numeros:
    print(numero)

# ------------------------------------------------------------
# Imprime el número más grande de la lista.
# ------------------------------------------------------------

print(f"\nEl número más grande es {valor_maximo}")