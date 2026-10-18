# ==================================================
# Práctica: Crear y Escribir Archivos 1
# Objetivo: Abrir el archivo "mi_archivo.txt" en modo
# escritura, reemplazar su contenido por "Nuevo texto"
# y luego imprimir el contenido actualizado.
# ==================================================

# --------------------------------------------------
# Abrir el archivo en modo escritura para reemplazar
# su contenido anterior
# --------------------------------------------------
mi_archivo = open("mi_archivo.txt", "w")

# --------------------------------------------------
# Escribir el nuevo texto en el archivo
# --------------------------------------------------
mi_archivo.write("Nuevo texto")

# --------------------------------------------------
# Cerrar el archivo después de escribir
# --------------------------------------------------
mi_archivo.close()

# --------------------------------------------------
# Volver a abrir el archivo en modo lectura
# --------------------------------------------------
mi_archivo = open("mi_archivo.txt", "r")

# --------------------------------------------------
# Leer e imprimir el contenido completo actualizado
# --------------------------------------------------
print(mi_archivo.read())

# --------------------------------------------------
# Cerrar el archivo después de leer
# --------------------------------------------------
mi_archivo.close()