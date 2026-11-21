# ==================================================
# Práctica: Módulos 1 - Módulo vacío
# Objetivo: Importar una función que está en otro
# módulo de la misma carpeta y ejecutarla.
# Se llama "vacío" porque no tiene funciones propias:
# todo lo que usa viene de modulo_ocupado.py.
# Estructura de la carpeta:
# mi_carpeta/
#     modulo_ocupado.py  -> tiene la función saludar()
#     modulo_vacio.py    -> importa y usa saludar()
# ==================================================


# --------------------------------------------------
# Importar la función saludar
# from modulo_ocupado import saludar trae solo la
# función saludar del módulo modulo_ocupado.py; se
# escribe el nombre del archivo sin la extensión .py.
# Como los dos archivos están en la misma carpeta,
# Python encuentra el módulo sin indicar ninguna ruta
# (por eso este archivo se debe ejecutar desde
# mi_carpeta)
# --------------------------------------------------
from modulo_ocupado import saludar

# --------------------------------------------------
# Usar la función importada
# Como se importó la función directamente, se llama
# con su nombre, sin anteponer el nombre del módulo.
# Imprime:
# Hola, estoy en el módulo ocupado.
# --------------------------------------------------
saludar()  # Llamada a la función para que se ejecute al importar el módulo
