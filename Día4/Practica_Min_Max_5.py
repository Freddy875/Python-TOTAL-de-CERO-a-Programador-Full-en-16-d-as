# ------------------------------------------------------------
# Práctica Min y Max 5
# Calcula la diferencia entre el valor máximo y el mínimo
# de una lista de números y almacena el resultado
# en una variable llamada rango.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de números que se utilizará para encontrar
# el valor máximo y el valor mínimo.
# ------------------------------------------------------------

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

# ------------------------------------------------------------
# Calcula el rango restando el valor mínimo al valor máximo.
# max() obtiene el número más grande.
# min() obtiene el número más pequeño.
# ------------------------------------------------------------

rango = max(lista_numeros) - min(lista_numeros)

# ------------------------------------------------------------
# Recorre la lista e imprime todos los números.
# ------------------------------------------------------------

for numero in lista_numeros:
    print(numero)

# ------------------------------------------------------------
# Muestra en una sola línea el número más grande,
# el número más pequeño y la diferencia entre ambos.
# ------------------------------------------------------------

print(
    f"El número más grande es {max(lista_numeros)}, "
    f"el número más pequeño es {min(lista_numeros)} "
    f"y la diferencia de ambos es {rango}"
)