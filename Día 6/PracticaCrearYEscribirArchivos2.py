# Abrir el archivo en modo "a" (append) para añadir una línea al final
mi_archivo = open("mi_archivo.txt", "a")
mi_archivo.write("Nuevo inicio de sesión")  # Agregamos la nueva línea
mi_archivo.close()  # Cerramos el archivo

# Volver a abrir el archivo en modo lectura ("r") y mostrar su contenido
mi_archivo = open("mi_archivo.txt", "r")
print(mi_archivo.read())  # Leer e imprimir el contenido actualizado
mi_archivo.close()  # Cerrar el archivo
