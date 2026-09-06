# ------------------------------------------------------------
# Programa: Tipos de datos en Python
#
# Este programa muestra cómo declarar variables de tipo
# entero (int) y decimal (float), realizar operaciones
# matemáticas básicas y verificar el tipo de dato de cada
# variable mediante la función type().
#
# Al final, solicita la edad del usuario utilizando input(),
# demostrando que los datos ingresados desde el teclado se
# almacenan como cadenas de texto (str).
# ------------------------------------------------------------


# ------------------------------------------------------------
# Declaración de variables enteras (int)
# Se crean variables de tipo entero, se muestran sus valores,
# su tipo de dato y el resultado de una suma.
# ------------------------------------------------------------

mi_numero1 = 1

print(mi_numero1)
print(type(mi_numero1))

mi_numero2 = 1 + 3

print(mi_numero2)
print(type(mi_numero2))

print(mi_numero1 + mi_numero2)


# ------------------------------------------------------------
# Declaración de variables decimales (float)
# Se crean variables con números decimales, se realizan
# operaciones aritméticas y se verifica su tipo de dato.
# ------------------------------------------------------------

mi_decimal1 = 5.81

print(mi_decimal1)
print(type(mi_decimal1))

mi_decimal2 = 5.81 + 5

print(mi_decimal2)
print(type(mi_decimal2))

mi_numero3 = 5.3 + 5.7

print(mi_numero3)
print(type(mi_numero3))


# ------------------------------------------------------------
# Entrada de datos por parte del usuario
# Se solicita la edad del usuario y se comprueba el tipo de
# dato devuelto por input(), el cual siempre es una cadena
# de texto (str).
# ------------------------------------------------------------

edad = input("Escribe tu edad: ")

print(type(edad))


# ------------------------------------------------------------
# Código de ejemplo (comentado)
# Estas líneas muestran un intento de sumar la edad ingresada
# con un número entero. No funcionan porque "edad" es una
# cadena de texto y primero debe convertirse a entero con int().
# ------------------------------------------------------------

### edad1 = 1

### print("El próximo año vas a tener", int(edad) + edad1)