# ------------------------------------------------------------
# Práctica Operadores Lógicos 5
#
# Crea tres variables (num1, num2 y num3):
# - Dentro de num1, almacena el valor 36.
# - Dentro de num2, almacena el resultado de la operación 72/2.
# - Dentro de num3, almacena el valor 48.
#
# Verifica si num1 es mayor que num2 o menor que num3.
# Almacena el resultado de dicha comparación.
# ------------------------------------------------------------

# Definir las variables

num1 = 36
num2 = 72 / 2  # Esto da 36
num3 = 48


# ------------------------------------------------------------
# Mostrar los valores de las variables
# Se muestran los valores obtenidos antes de realizar
# las comparaciones.
# ------------------------------------------------------------

print(f"El número 1 es: {num1}")
print(f"El número 2 es el resultado de 72 / 2: {num2}")
print(f"El número 3 es: {num3}")


# ------------------------------------------------------------
# Verificar la primera condición
# Se comprueba si el número 1 es mayor que el número 2.
# ------------------------------------------------------------

print(f"\nEl número 1 es {num1} y el número 2 es {num2}.")
print(f"¿El número 1 es mayor que el número 2? {'Sí' if num1 > num2 else 'No'}")


# ------------------------------------------------------------
# Verificar la segunda condición
# Se comprueba si el número 1 es menor que el número 3.
# ------------------------------------------------------------

print(f"\nEl número 1 es {num1} y el número 3 es {num3}.")
print(f"¿El número 1 es menor que el número 3? {'Sí' if num1 < num3 else 'No'}")


# ------------------------------------------------------------
# Verificar si se cumple alguna de las dos condiciones
# El operador or devuelve True cuando al menos una de las
# condiciones es verdadera.
# ------------------------------------------------------------

# Verificar si num1 es mayor que num2 o menor que num3

mi_bool = num1 > num2 or num1 < num3


# ------------------------------------------------------------
# Mostrar la conclusión
# Se utiliza la condición final para explicar al usuario
# cuál de las dos condiciones se cumple.
# ------------------------------------------------------------

print("\nPor lo tanto:")

if mi_bool:
    print(f"\nTienes ${num1}, el producto cuesta ${num2} y tu límite de compra es ${num3}.")

    if num1 > num2:
        print("Tienes más dinero que el precio del producto, por lo tanto puedes comprarlo.")
    elif num1 < num3:
        print("El precio está dentro de tu límite de compra, por lo tanto puedes comprarlo.")
else:
    print("No se cumple ninguna de las condiciones, por lo tanto no puedes comprarlo.")