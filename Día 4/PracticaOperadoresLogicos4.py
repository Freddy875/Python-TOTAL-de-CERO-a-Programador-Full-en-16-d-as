# Definir las variables

num1 = 36
num2 = 72 / 2
num3 = 48


# Mostrar los valores de las variables

print(f"El número 1 es: {num1}")
print(f"El número 2 es el resultado de 72 / 2: {num2}")
print(f"El número 3 es: {num3}")

# Comparar el número 1 con el número 2

print(f"\nEl número 1 es {num1} y el número 2 es {num2}.")
print(f"¿El número 1 es mayor que el número 2? {'Sí' if num1 > num2 else 'No'}")


# Comparar el número 1 con el número 3

print(f"\nEl número 1 es {num1} y el número 3 es {num3}.")
print(f"¿El número 1 es menor que el número 3? {'Sí' if num1 < num3 else 'No'}")


# ------------------------------------------------------------
# Verificar las dos condiciones
# El operador and exige que ambas condiciones sean verdaderas.
# En este caso, para ganar se deben cumplir las dos condiciones:
# tener más puntos que el otro jugador y no superar los 48 puntos.
# ------------------------------------------------------------

mi_bool = num1 > num2 and num1 < num3


# ------------------------------------------------------------
# Mostrar la conclusión
# Para ganar, el número 1 debe ser mayor que el número 2
# y menor que el número 3.
# Como ambos tienen la misma puntuación, el número 1 no es
# mayor que el número 2, por lo que no se cumplen ambas
# condiciones.
# ------------------------------------------------------------

print("\nPor lo tanto:")

if mi_bool:
    print(f"Tienes {num1} puntos, más que el otro jugador ({num2}),")
    print(f"y estás por debajo del límite de {num3} puntos.")
    print("¡Ganaste!")
else:
    print(f"Tienes {num1} puntos y el otro jugador tiene {num2}.")
    print(f"Ambos están por debajo del límite de {num3} puntos.")
    print("Ninguno gana porque tienen la misma puntuación.")