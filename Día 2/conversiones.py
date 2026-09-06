# ------------------------------------------------------------
# Programa: Conversión de tipos de datos en Python
#
# Este programa muestra la diferencia entre la conversión
# implícita y la conversión explícita de tipos de datos.
# También solicita la edad del usuario, la convierte a un
# número entero y realiza una operación aritmética con ella.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Conversión implícita
# Python convierte automáticamente un número entero (int)
# a un número decimal (float) al realizar una operación
# entre ambos tipos de datos.
# ------------------------------------------------------------

num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))


# ------------------------------------------------------------
# Conversión explícita
# Se convierte un número decimal (float) a un número entero
# (int) utilizando la función int() y se muestra el cambio
# del tipo de dato en pantalla.
# ------------------------------------------------------------

num3 = 5.8

print(num3)
print(type(num3))

num4 = int(num3)

print(num4)
print(type(num4))


# ------------------------------------------------------------
# Conversión y operación con la edad del usuario
# Se solicita la edad del usuario mediante input(), se
# convierte el dato a un número entero para poder realizar
# operaciones matemáticas y se calcula la edad que tendrá
# el próximo año.
# ------------------------------------------------------------

edad = input("Ingresa tu edad: ")

edad = int(edad)

print(type(edad))

nueva_edad = edad + 1

print(f"El próximo año tendrás: {nueva_edad}")