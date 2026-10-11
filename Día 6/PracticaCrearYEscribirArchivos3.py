# Lista con los datos de la última sesión
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Abrir el archivo en modo "a" (append) para añadir la línea al final
with open("registro.txt", "a") as archivo:
    archivo.writelines("\t".join(registro_ultima_sesion) + "\n")  # Convertir la lista a un string separado por tabuladores

# Volver a abrir el archivo en modo lectura ("r") y mostrar su contenido
with open("registro.txt", "r") as archivo:
    print(archivo.read())  # Leer e imprimir el contenido actualizado