# ------------------------------------------------------------
# Práctica Min y Max 1
# Obtiene el valor máximo entre los valores de una lista
# y lo almacena en la variable valor_maximo.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de números.
# Cada elemento puede contener diferentes operaciones
# matemáticas que Python calculará antes de comparar los valores.
# ------------------------------------------------------------

lista_numeros = [
    44542247 / 2,
    21310 / 5,
    2134747 * 33,
    44556475,
    121676,
    6654067,
    353254,
    123134,
    55 ** 12,
    611 ** 5
]

# ------------------------------------------------------------
# max() busca el valor más grande dentro de la lista
# y lo almacena en la variable valor_maximo.
# ------------------------------------------------------------

valor_maximo = max(lista_numeros)

# ------------------------------------------------------------
# Imprime el valor máximo encontrado en la lista.
# ------------------------------------------------------------

print(valor_maximo)