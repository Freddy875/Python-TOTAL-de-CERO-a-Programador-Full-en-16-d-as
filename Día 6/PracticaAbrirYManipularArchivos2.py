# ==================================================
# Práctica: Abrir y Manipular Archivos 2
# Objetivo: Abrir el archivo "texto.txt", leer e
# imprimir únicamente la primera línea y cerrar
# el archivo después de utilizarlo.
# ==================================================

# --------------------------------------------------
# Abrir el archivo en modo lectura
# --------------------------------------------------
mi_archivo = open("texto.txt", "r")

# --------------------------------------------------
# Leer e imprimir la primera línea del archivo
# --------------------------------------------------
print(mi_archivo.readline())

# --------------------------------------------------
# Cerrar el archivo después de utilizarlo
# --------------------------------------------------
mi_archivo.close()
