def sobrescribir(archivo):
        archivo_sobrescribir = open(archivo, "w")  # Abrir en modo escritura
        archivo_sobrescribir.write("contenido eliminado")  # Sobrescribir el contenido
        archivo_sobrescribir.close()  # Cerrar el archivo
    
# Ejemplo de uso:
sobrescribir("ejemplo.txt")  # Llamar la función para sobrescribir el archivo
    
# Verificar el contenido después de sobrescribir
archivo_verificar = open("ejemplo.txt", "r")
print(archivo_verificar.read())  # Debería imprimir "contenido eliminado"
archivo_verificar.close()  # Cerrar el archivo después de leerlo