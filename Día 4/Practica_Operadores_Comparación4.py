# ------------------------------------------------------------
# Práctica Operadores de Comparación 3
#
# Crea dos variables (num1 y num2):
# - Dentro de num1, almacena el resultado de la operación 64 x 3.
# - Dentro de num2, almacena el resultado de la operación 24 x 8.
#
# Verifica si num1 es diferente a num2 y almacena el resultado
# de dicha comparación en una variable llamada mi_bool.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Mostrar las operaciones antes de ejecutarlas
# Se muestran las operaciones que vamos a realizar.
# ------------------------------------------------------------

print("Primera operación: 64 x 3")
print("Segunda operación: 24 x 8")


# ------------------------------------------------------------
# Definir las variables
# Se realizan las operaciones y se almacenan sus resultados
# en num1 y num2.
# ------------------------------------------------------------

num1 = 64 * 3
num2 = 24 * 8


# ------------------------------------------------------------
# Mostrar los resultados de las operaciones
# Se muestran los valores obtenidos después de realizar
# las multiplicaciones.
# ------------------------------------------------------------

print(f"El resultado de la primera operación es: {num1}")
print(f"El resultado de la segunda operación es: {num2}")


# ------------------------------------------------------------
# Verificar si num1 es diferente a num2
# El operador != comprueba si los dos valores son diferentes.
# El resultado de la comparación se almacena en mi_bool.
# ------------------------------------------------------------

mi_bool = num1 != num2


# ------------------------------------------------------------
# Mostrar el resultado de la comparación
# Se utiliza if para mostrar un mensaje que explique el
# resultado de la comparación de forma clara.
# ------------------------------------------------------------

if mi_bool:
    print("Por lo tanto, los números son diferentes.")
else:
    print("Por lo tanto, los números son iguales.")