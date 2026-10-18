# ------------------------------------------------------------
# Este programa utiliza el método insert() para agregar
# dinosaurios en posiciones específicas de una lista.
# A diferencia de append(), insert() permite elegir el índice
# donde se colocará el nuevo elemento.
# ------------------------------------------------------------

dinosaurios = ["Spinosaurio", "Carnotauro", "Brachiosaurio", "Velociraptor"]


# ------------------------------------------------------------
# Insertar T-Rex
# El índice 3 corresponde a la posición anterior a
# "Spinosaurio", por lo que T-Rex antes de este".
# ------------------------------------------------------------

dinosaurios.insert(0, "T-Rex")


# ------------------------------------------------------------
# Insertar Triceratops
# Después de insertar T-Rex, el índice 4 corresponde a la
# posición anterior a "Velociraptor".
# ------------------------------------------------------------

dinosaurios.insert(4, "Triceratops")


# ------------------------------------------------------------
# Insertar Iguanodon
# Después de las inserciones anteriores, el índice 5
# corresponde a la posición anterior a "Velociraptor".
# ------------------------------------------------------------

dinosaurios.insert(5, "Iguanodon")


# ------------------------------------------------------------
# Mostrar la lista
# Se muestra la lista con los nuevos dinosaurios en el orden
# en que fueron insertados.
# ------------------------------------------------------------

print(dinosaurios)