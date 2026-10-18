# ------------------------------------------------------------
# Práctica Enumerador 2
# Crea una lista formada por tuplas (índice, elemento),
# utilizando enumerate() para obtener el índice de cada
# carácter del string "Python".
# ------------------------------------------------------------

# ------------------------------------------------------------
# String base que se recorrerá con enumerate().
# ------------------------------------------------------------

palabra = "Python"

# ------------------------------------------------------------
# enumerate() obtiene el índice y el carácter correspondiente.
# list() convierte el resultado de enumerate() en una lista.
# Cada elemento de la lista será una tupla:
# (índice, carácter).
# ------------------------------------------------------------

lista_indices = list(enumerate(palabra))

# ------------------------------------------------------------
# Imprime la lista de tuplas obtenida.
# ------------------------------------------------------------

print(lista_indices)