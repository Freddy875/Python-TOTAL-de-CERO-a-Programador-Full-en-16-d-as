# ------------------------------------------------------------
# Práctica Enumerador 4
# Imprime el nombre y el índice de aquellos nombres de la lista
# que comienzan con la letra "M".
# Para resolverlo se utiliza un loop, enumerate(),
# un condicional if y el método startswith().
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de nombres que se recorrerá.
# ------------------------------------------------------------

lista_nombres = [
    "Marcos",
    "Laura",
    "Mónica",
    "Javier",
    "Celina",
    "Marta",
    "Darío",
    "Emiliano",
    "Melisa"
]

# ------------------------------------------------------------
# Loop con enumerate()
# Obtiene el índice y el nombre de cada elemento de la lista.
# ------------------------------------------------------------

for indice, nombre in enumerate(lista_nombres):

    # --------------------------------------------------------
    # Verifica si el nombre comienza con la letra "M".
    # startswith("M") devuelve True cuando el nombre
    # comienza con la letra "M".
    # --------------------------------------------------------

    if nombre.startswith("M"):

        # ----------------------------------------------------
        # Imprime el nombre y el índice donde se encuentra.
        # ----------------------------------------------------

        print(f"{nombre} se encuentra en el índice {indice}")