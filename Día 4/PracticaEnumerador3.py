# ------------------------------------------------------------
# Práctica Enumerador 3
# Imprime únicamente los índices de aquellos nombres de la lista
# que comiencen con la letra "M".
# Para resolverlo se utiliza un loop, enumerate() y un condicional if.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de nombres que se recorrerá.
# ------------------------------------------------------------

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


# ------------------------------------------------------------
# Loop con enumerate()
# enumerate() permite obtener el índice y el nombre
# correspondiente en cada vuelta.
# ------------------------------------------------------------

for indice, nombre in enumerate(lista_nombres):

    # --------------------------------------------------------
    # Verifica si el nombre comienza con la letra "M".
    # startswith("M") devuelve True si comienza con "M".
    # --------------------------------------------------------

    if nombre.startswith("M"):

        # ----------------------------------------------------
        # Imprime únicamente el índice del nombre que
        # comienza con la letra "M".
        # ----------------------------------------------------

        print(indice)