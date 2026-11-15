# ==================================================
# Práctica: Crear y Escribir Archivos 2
# Objetivo: Abrir el archivo "mi_archivo.txt" en modo
# añadir, agregar una nueva línea al final y después
# imprimir todo el contenido actualizado del archivo.
# ==================================================

# --------------------------------------------------
# Abrir el archivo en modo "a" (append) para añadir
# contenido al final sin borrar el texto existente
# --------------------------------------------------
mi_archivo = open("mi_archivo.txt", "a")

# --------------------------------------------------
# Escribir el nuevo texto al final del archivo
# --------------------------------------------------
mi_archivo.write("\nNuevo inicio de sesión")

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