mi_archivo = open("prueba.txt", "r")

print(type(mi_archivo))

# ----------------------------------------
# LEER LAS PRIMERAS TRES LÍNEAS
# ----------------------------------------

primera_linea = mi_archivo.readline()
print(primera_linea.upper())

primera_linea = mi_archivo.readline()
print(primera_linea)

primera_linea = mi_archivo.readline()
print(primera_linea)


# ----------------------------------------
# LEER LAS LÍNEAS RESTANTES Y GUARDARLAS
# ----------------------------------------

# Guarda en una lista todas las líneas que todavía no se han leído.
todas_las_lineas = mi_archivo.readlines()

# Muestra la lista con las líneas restantes.
print("Todas las líneas restantes:")
print(todas_las_lineas)


# ----------------------------------------
# CERRAR EL ARCHIVO
# ----------------------------------------

mi_archivo.close()