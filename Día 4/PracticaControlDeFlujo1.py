# ------------------------------------------------------------
# Práctica Control de Flujo 1
#
# Utilizando las variables num1 y num2, que reciben valores
# mediante input(), crea una estructura de control de flujo
# que compare ambos valores y muestre un resultado según
# el caso:
#
# - num1 es mayor que num2.
# - num2 es mayor que num1.
# - num1 y num2 son iguales.
#
# Deben mostrarse los valores ingresados por el usuario
# en lugar de escribir literalmente num1 y num2.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Solicitar los números al usuario
#
# Se utiliza input() para solicitar dos números al usuario.
# int() convierte los valores ingresados de texto a números
# enteros para poder realizar las comparaciones.
# ------------------------------------------------------------

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


# ------------------------------------------------------------
# Comparar los valores
#
# Se utiliza if para comprobar si num1 es mayor que num2.
# elif comprueba si num2 es mayor que num1.
# Si ninguna de las dos condiciones anteriores se cumple,
# significa que ambos valores son iguales y se ejecuta else.
# ------------------------------------------------------------

if num1 > num2:
    print(f"{num1} es mayor que {num2}")

elif num2 > num1:
    print(f"{num2} es mayor que {num1}")

else:
    print(f"{num1} y {num2} son iguales")