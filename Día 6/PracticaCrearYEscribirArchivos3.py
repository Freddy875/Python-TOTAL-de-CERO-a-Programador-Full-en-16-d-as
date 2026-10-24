# ==================================================
# Práctica: Crear y Escribir Archivos 3
# Objetivo: Utilizar el método writelines() para
# agregar los datos de una lista al final del archivo
# "registro.txt", separando cada elemento con un
# tabulador, y después imprimir todo su contenido.
# ==================================================

# --------------------------------------------------
# Crear una lista con los datos de la última sesión
# --------------------------------------------------
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# --------------------------------------------------
# Abrir el archivo en modo "a" (append) para añadir
# los datos al final sin borrar el contenido anterior
# --------------------------------------------------
with open("registro.txt", "a") as archivo:

    # Unir los elementos de la lista con tabuladores
    # y agregar un salto de línea al final
    archivo.writelines("\t".join(registro_ultima_sesion) + "\n")

# --------------------------------------------------
# Volver a abrir el archivo en modo lectura
# --------------------------------------------------
with open("registro.txt", "r") as archivo:

    # Leer e imprimir el contenido completo
    print(archivo.read())