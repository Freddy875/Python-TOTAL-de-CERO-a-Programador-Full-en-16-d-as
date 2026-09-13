# Definir las variables

num1 = 36
num2 = 72 / 2
num3 = 48


# Mostrar los valores de las variables

print(f"El número 1 es: {num1}")
print(f"El número 2 es el resultado de 72 / 2: {num2}")
print(f"El número 3 es: {num3}")


# Comparar el número 1 con el número 2

print(f"\n¿El número 1 ({num1}) es mayor que el número 2 ({num2})?")
print("Sí" if num1 > num2 else "No")


# Comparar el número 1 con el número 3

print(f"\n¿El número 1 ({num1}) es menor que el número 3 ({num3})?")
print("Sí" if num1 < num3 else "No")


# Verificar las dos condiciones

mi_bool = num1 > num2 and num1 < num3

print("\nPor lo tanto:")

if mi_bool:
    print("El número 1 es mayor que el número 2 y menor que el número 3.")
else:
    print("El número 1 no es mayor que el número 2 y menor que el número 3.")