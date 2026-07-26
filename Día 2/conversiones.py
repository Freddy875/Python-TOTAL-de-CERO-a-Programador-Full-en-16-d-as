# ------------------------------------------------------------
# Converisión explcita
# ------------------------------------------------------------

num1 = 20

num2 = 30.5

num1 = num1 + num2

print(type(num1))

print(type(num2))

# ------------------------------------------------------------
# Converisión implicita
# ------------------------------------------------------------


num3 = 5.8

print(num3)

print(type(num3))

num4 = int(num3)

print(num4)

print(type(num4))

edad = input("Ingresa tu edad: ")

edad = int(edad)

print(type(edad))

nueva_edad = edad + 1

print("El proximo año tendras: " + nueva_edad)