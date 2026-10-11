mi_archivo = open("texto.txt", "r")

# Leer y descartar la primera línea
mi_archivo.readline()

# Leer e imprimir la segunda línea
print(mi_archivo.readline())

# Cerrar el archivo
mi_archivo.close()