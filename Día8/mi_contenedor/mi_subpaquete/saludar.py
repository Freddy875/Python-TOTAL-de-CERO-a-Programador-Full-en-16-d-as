# ==================================================
# Práctica: Paquetes - Módulo saludar
# Objetivo: Crear un módulo dentro del paquete
# mi_subpaquete con una función que imprime un saludo,
# para usarla desde ejercicios.py.
# Ruta: mi_contenedor/mi_subpaquete/saludar.py
# ==================================================


# --------------------------------------------------
# Definir la función saludar
# Tiene el mismo nombre que el módulo (saludar.py);
# por eso, al importar el módulo, se llama con
# saludar.saludar(): el primero es el módulo y el
# segundo es la función. Imprime:
# Hola, mundo
# --------------------------------------------------
def saludar():
    """Imprime el saludo Hola, mundo."""
    print("Hola, mundo")
