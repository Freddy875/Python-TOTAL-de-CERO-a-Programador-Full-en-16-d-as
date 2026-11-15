# ------------------------------------------------------------
# Práctica Enumerador 1
# Imprime cada nombre de la lista junto con el índice
# en el que se encuentra.
# El índice se obtiene utilizando enumerate().
# ------------------------------------------------------------

# ------------------------------------------------------------
# Lista de nombres que se recorrerá.
# ------------------------------------------------------------

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# ------------------------------------------------------------
# Loop con enumerate()
# enumerate() permite obtener dos datos en cada vuelta:
# indice: posición que ocupa el nombre en la lista.
# nombre: elemento actual de la lista.
# ------------------------------------------------------------

for indice, nombre in enumerate(lista_nombres):

    # --------------------------------------------------------
    # Muestra el nombre junto con el índice donde se encuentra.
    # --------------------------------------------------------

    print(f"{nombre} se encuentra en el índice {indice}")

    