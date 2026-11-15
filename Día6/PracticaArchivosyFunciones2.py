# ==================================================
# Práctica: Archivos y Funciones 2
# Objetivo: Crear una función llamada sobrescribir() que
# abra (open) un archivo indicado como parámetro y
# sobrescriba cualquier contenido anterior por el texto
# "contenido eliminado", y después verificar el resultado
# leyendo el archivo.
# ==================================================

# --------------------------------------------------
# Definir la función sobrescribir()
# --------------------------------------------------
def sobrescribir(archivo):
        """Sobrescribe el contenido de un archivo con "contenido eliminado".

        Parámetros:
            archivo: nombre o ruta del archivo a sobrescribir.
        """
        # Abrir el archivo en modo escritura ("w"); si ya existe, se
        # borra todo su contenido anterior, y si no existe, se crea
        archivo_sobrescribir = open(archivo, "w")  # Abrir en modo escritura

        # Escribir el nuevo texto, que reemplaza todo lo anterior
        archivo_sobrescribir.write("contenido eliminado")  # Sobrescribir el contenido

        # Cerrar el archivo para guardar los cambios y liberar el recurso
        archivo_sobrescribir.close()  # Cerrar el archivo
    
# --------------------------------------------------
# Ejemplo de uso de la función
# --------------------------------------------------
sobrescribir("ejemplo.txt")  # Llamar la función para sobrescribir el archivo
    
# --------------------------------------------------
# Verificar el contenido después de sobrescribir
# Abrir el archivo en modo lectura ("r") para comprobar el cambio
# --------------------------------------------------
archivo_verificar = open("ejemplo.txt", "r")

# Leer e imprimir todo el contenido del archivo
print(archivo_verificar.read())  # Debería imprimir "contenido eliminado"

# Cerrar el archivo después de leerlo
archivo_verificar.close()  # Cerrar el archivo después de leerlo