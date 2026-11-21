# ==================================================
# Práctica: Paquetes - Programa principal
# Objetivo: Usar módulos que están guardados en dos
# paquetes distintos: saludar al usuario, pedirle dos
# números y mostrar su suma y su resta.
# mi_contenedor es la carpeta que agrupa el programa y
# los paquetes; este archivo se debe ejecutar desde
# mi_contenedor para que Python encuentre los paquetes.
# Estructura de la carpeta:
# mi_contenedor/
#     ejercicios.py        -> programa principal
#     mi_paquete/          -> paquete
#         __init__.py
#         suma_resta.py    -> funciones suma() y resta()
#     mi_subpaquete/       -> paquete
#         __init__.py
#         saludar.py       -> función saludar()
# ==================================================


# --------------------------------------------------
# Importar los módulos de los paquetes
# from <paquete> import <módulo> trae el módulo
# completo; para usar sus funciones se escribe el
# nombre del módulo, un punto y el nombre de la
# función, por ejemplo: suma_resta.suma()
# --------------------------------------------------
from mi_paquete import suma_resta
from mi_subpaquete import saludar

# --------------------------------------------------
# Saludar al usuario
# saludar.saludar() llama a la función saludar del
# módulo saludar; imprime:
# Hola, mundo
# --------------------------------------------------
saludar.saludar()  # Llama a la función saludar del módulo saludar.py

# --------------------------------------------------
# Pedir los dos números
# input() pide el dato como texto y float() lo
# convierte a decimal; se guardan en las variables
# numero1 y numero2
# --------------------------------------------------
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# --------------------------------------------------
# Calcular y mostrar la suma
# La variable resultado_suma guarda lo que devuelve
# suma_resta.suma(). Si el usuario escribe 8 y 3,
# imprime:
# La suma de 8.0 y 3.0 es: 11.0
# --------------------------------------------------
resultado_suma = suma_resta.suma(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es: {resultado_suma}")

# --------------------------------------------------
# Calcular y mostrar la resta
# La variable resultado_resta guarda lo que devuelve
# suma_resta.resta(). Si el usuario escribe 8 y 3,
# imprime:
# La resta de 8.0 y 3.0 es: 5.0
# --------------------------------------------------
resultado_resta = suma_resta.resta(numero1, numero2)
print(f"La resta de {numero1} y {numero2} es: {resultado_resta}")
