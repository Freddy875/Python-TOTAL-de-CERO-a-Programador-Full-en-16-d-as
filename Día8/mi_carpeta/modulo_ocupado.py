# ==================================================
# Práctica: Módulos 1 - Módulo ocupado
# Objetivo: Crear un módulo, es decir, un archivo .py
# que guarda código (en este caso, una función) para
# que otro archivo lo pueda importar y usar.
# Este módulo vive en la carpeta mi_carpeta junto con
# modulo_vacio.py, que es el archivo que lo importa.
# ==================================================


# --------------------------------------------------
# Definir la función saludar
# Imprime un saludo para comprobar que el código de
# este módulo se puede usar desde otro archivo.
# Al llamarla, imprime:
# Hola, estoy en el módulo ocupado.
# --------------------------------------------------
def saludar():
    """Imprime un saludo desde el módulo ocupado."""
    print("Hola, estoy en el módulo ocupado.")
