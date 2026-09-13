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


# Verificar las dos condiciones

mi_bool = num1 > num2 and num1 < num3

print("\nPor lo tanto:")

if mi_bool:
    print(f"El número 1 ({num1}) es mayor que el número 2 ({num2}) y menor que el número 3 ({num3}).")
else:
    print(f"El número 1 ({num1}) no es mayor que el número 2 ({num2}), pero sí es menor que el número 3 ({num3}).")