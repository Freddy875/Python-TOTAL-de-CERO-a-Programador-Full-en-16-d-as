# ==================================================
# Práctica: Abrir y Manipular Archivos 1
# Objetivo: Abrir el archivo "texto.txt", leer e
# imprimir todo su contenido en la consola y cerrarlo
# al finalizar la lectura.
# ==================================================

# --------------------------------------------------
# Abrir el archivo en modo lectura
# --------------------------------------------------
archivo = open("texto.txt", "r")

# --------------------------------------------------
# Leer e imprimir todo el contenido del archivo
# --------------------------------------------------
print(archivo.read())

# --------------------------------------------------
# Cerrar el archivo después de leerlo
# --------------------------------------------------
archivo.close()