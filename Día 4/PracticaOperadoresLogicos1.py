# ------------------------------------------------------------
# Práctica Operadores Lógicos 1
#
# Crea tres variables (num1, num2 y num3):
# - Dentro de num1, almacena el valor 36.
# - Dentro de num2, almacena el resultado de la operación 72/2.
# - Dentro de num3, almacena el valor 48.
#
# Verifica si num1 es mayor que num2, y menor que num3.
# Almacena el resultado de dicha comparación en una variable
# llamada mi_bool.
# ------------------------------------------------------------

# Definir las variables

num1 = 36
num2 = 72 / 2  # Esto da 36
num3 = 48

# ------------------------------------------------------------
# Verificar las condiciones
# Se utiliza el operador and para comprobar que ambas
# condiciones se cumplan al mismo tiempo:
# num1 debe ser mayor que num2 y menor que num3.
# El resultado se almacena en mi_bool.
# ------------------------------------------------------------

# Verificar si num1 es mayor que num2 y menor que num3

mi_bool = num1 > num2 and num1 < num3

# ------------------------------------------------------------
# Imprimir el resultado
# Se muestra el valor booleano obtenido de las condiciones.
# ------------------------------------------------------------

# Imprimir el resultado

print(mi_bool)  # Esto imprimirá False