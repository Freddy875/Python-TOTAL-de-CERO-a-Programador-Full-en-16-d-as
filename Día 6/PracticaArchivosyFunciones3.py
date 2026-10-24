# ==================================================
# Práctica: Archivos y Funciones 3
# Objetivo: Crear una función llamada registro_error() que
# abra (open) un archivo indicado como parámetro y lo
# actualice añadiendo al final el texto "se ha registrado
# un error de ejecución", cerrando el archivo al terminar.
# ==================================================

# --------------------------------------------------
# Definir la función registro_error()
# --------------------------------------------------
def registro_error(archivo):
    """Añade al final de un archivo el texto "se ha registrado un error de ejecución".

    Parámetros:
        archivo: nombre o ruta del archivo a actualizar.
    """
    # Abrir el archivo en modo "a" (append): el texto se agrega al
    # final sin borrar el contenido anterior, y si el archivo no
    # existe, se crea; with lo cierra automáticamente al terminar
    with open(archivo, "a") as mi_archivo:

            # Escribir el texto al final del archivo
            mi_archivo.write("se ha registrado un error de ejecución")