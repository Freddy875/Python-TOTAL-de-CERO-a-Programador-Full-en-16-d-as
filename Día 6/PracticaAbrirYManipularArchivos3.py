# ==================================================
# Práctica: Abrir y Manipular Archivos 3
# Objetivo: Abrir el archivo "texto.txt" y leer e
# imprimir únicamente la segunda línea de su contenido.
# ==================================================

# --------------------------------------------------
# Abrir el archivo en modo lectura
# --------------------------------------------------
mi_archivo = open("texto.txt", "r")

# --------------------------------------------------
# Leer y descartar la primera línea
# --------------------------------------------------
mi_archivo.readline()

# --------------------------------------------------
# Leer e imprimir la segunda línea
# --------------------------------------------------
print(mi_archivo.readline())

# --------------------------------------------------
# Cerrar el archivo después de utilizarlo
# --------------------------------------------------
mi_archivo.close()