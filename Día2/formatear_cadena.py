# ------------------------------------------------------------
# Programa: Formateo de cadenas de texto en Python
#
# Este programa muestra diferentes formas de combinar texto
# con variables utilizando concatenación, el método format()
# y las f-strings. Finalmente, solicita al usuario la marca
# y el color de su coche para mostrar un mensaje
# personalizado.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Declaración de variables numéricas
# Se crean dos variables enteras que serán utilizadas en los
# ejemplos de formateo de cadenas de texto.
# ------------------------------------------------------------

num1 = 10
num2 = 5


# ------------------------------------------------------------
# Concatenación de cadenas
# Se utiliza el operador + para unir texto con variables.
# Como las variables son de tipo entero, es necesario
# convertirlas previamente a cadenas de texto mediante str().
# ------------------------------------------------------------

print("Mis números son: " + str(num1) + " y " + str(num2))


# ------------------------------------------------------------
# Formateo de cadenas con el método format()
# Este método permite insertar valores dentro de una cadena
# utilizando llaves {} como marcadores de posición.
# ------------------------------------------------------------

print("Mis números son: {} y {}".format(num1, num2))

print("Mis números son: {} y {}".format(num2, num1))

print("Mis números son: {} y {}".format(563, 480))

print("Mis números son: {} y {} y la suma es: {}".format(num1, num2, num1 + num2))

print("Mis números son: {} y {} y la suma es: {}".format(563, 480, 563 + 480))


# ------------------------------------------------------------
# Entrada de datos del usuario
# Se solicita al usuario la marca y el color de su coche.
# Posteriormente, se muestra un mensaje personalizado
# utilizando una f-string.
# ------------------------------------------------------------

marca = input("¿Cuál es la marca de tu coche? ")
color = input("¿De qué color es tu coche? ")

print(f"Tu coche es un {marca} de color {color}.")