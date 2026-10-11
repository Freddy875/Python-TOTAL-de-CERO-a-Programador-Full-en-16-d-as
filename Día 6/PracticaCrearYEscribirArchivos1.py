# Abrir el archivo en modo escritura ("w") y reemplazar su contenido
mi_archivo = open("mi_archivo.txt", "w")
mi_archivo.write("Nuevo texto")  # Escribimos el nuevo contenido
mi_archivo.close()  # Cerramos el archivo

# Volver a abrir el archivo en modo lectura ("r") y mostrar su contenido
mi_archivo = open("mi_archivo.txt", "r")
print(mi_archivo.read())  # Leer e imprimir el contenido actualizado
mi_archivo.close()  # Cerrar el archivo
