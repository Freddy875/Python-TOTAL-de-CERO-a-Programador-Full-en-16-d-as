def registro_error(archivo):
    with open(archivo, "a") as mi_archivo:
            mi_archivo.write("se ha registrado un error de ejecución")
