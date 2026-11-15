# ------------------------------------------------------------
# Práctica Operadores de Comparación 2
#
# Crea dos variables (num1 y num2):
# - Dentro de num1, almacena el resultado de la operación
#   raíz cuadrada de 25.
# - Dentro de num2, almacena el número 5.
#
# Verifica si num1 es igual a num2 y almacena el resultado
# de dicha comparación en una variable llamada mi_bool.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Importar el módulo math
# Se importa el módulo math para utilizar sqrt(), que permite
# calcular la raíz cuadrada de un número.
# ------------------------------------------------------------

import math


# ------------------------------------------------------------
# Definir las variables
# Se calcula la raíz cuadrada de 25 y se almacena el resultado
# en num1. En num2 se almacena el número 5.
# ------------------------------------------------------------

num1 = math.sqrt(25)
num2 = 5


# ------------------------------------------------------------
# Verificar si num1 es igual a num2
# El operador == comprueba si ambos valores son iguales.
# El resultado de la comparación se almacena en mi_bool.
# ------------------------------------------------------------

mi_bool = num1 == num2


# ------------------------------------------------------------
# Imprimir el resultado
# Se muestra el valor booleano obtenido de la comparación.
# ------------------------------------------------------------

print(mi_bool)
# Imprime: True