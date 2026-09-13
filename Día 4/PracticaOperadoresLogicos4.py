# Definir las variables

num1 = 36
num2 = 72 / 2
num3 = 48

print(f"num1 es: {num1}")
print(f"num2 es: 72 / 2 = {num2}")
print(f"num3 es: {num3}")


# Verificar si num1 es mayor que num2 y menor que num3

print(f"\n¿num1 ({num1}) es mayor que num2 ({num2})?")
print(num1 > num2)

print(f"\n¿num1 ({num1}) es menor que num3 ({num3})?")
print(num1 < num3)

mi_bool = num1 > num2 and num1 < num3

print(f"\nPor lo tanto, ¿num1 es mayor que num2 y menor que num3?")
print(mi_bool)