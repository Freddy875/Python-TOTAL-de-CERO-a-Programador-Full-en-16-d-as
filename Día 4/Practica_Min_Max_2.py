# ------------------------------------------------------------
# Práctica Min y Max 2
# Calcula la diferencia entre el valor máximo y el mínimo
# de una lista de números y almacena el resultado
# en la variable rango.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de números que se utilizará para encontrar
# el valor máximo y el valor mínimo.
# ------------------------------------------------------------

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

# ------------------------------------------------------------
# Calcula el rango restando el valor mínimo al valor máximo.
# max() obtiene el número más grande de la lista.
# min() obtiene el número más pequeño de la lista.
# ------------------------------------------------------------

rango = max(lista_numeros) - min(lista_numeros)

# ------------------------------------------------------------
# Imprime el resultado de la diferencia entre el máximo
# y el mínimo.
# ------------------------------------------------------------

print(rango)