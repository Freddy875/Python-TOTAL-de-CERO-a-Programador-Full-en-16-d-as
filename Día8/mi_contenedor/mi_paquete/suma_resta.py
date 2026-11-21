# ==================================================
# Práctica: Paquetes - Módulo suma_resta
# Objetivo: Crear un módulo dentro del paquete
# mi_paquete con dos funciones matemáticas, suma y
# resta, para usarlas desde ejercicios.py.
# Ruta: mi_contenedor/mi_paquete/suma_resta.py
# ==================================================


# --------------------------------------------------
# Definir la función suma
# Recibe dos números y return devuelve su suma.
# Por ejemplo, suma(8, 3) devuelve 11
# --------------------------------------------------
def suma(numero1, numero2):
    """Suma dos números.

    Parámetros:
        numero1: primer número a sumar (decimal).
        numero2: segundo número a sumar (decimal).

    Devuelve:
        La suma de los dos números (decimal).
    """
    return numero1 + numero2


# --------------------------------------------------
# Definir la función resta
# Recibe dos números y return devuelve el resultado de
# restar el segundo al primero.
# Por ejemplo, resta(8, 3) devuelve 5
# --------------------------------------------------
def resta(numero1, numero2):
    """Resta dos números.

    Parámetros:
        numero1: primer número (decimal).
        numero2: número que se resta del primero (decimal).

    Devuelve:
        La resta de los dos números (decimal).
    """
    return numero1 - numero2
