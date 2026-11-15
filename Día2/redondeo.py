# ------------------------------------------------------------
# Programa: Redondeo de números en Python
#
# Este programa muestra diferentes formas de utilizar la
# función round() para redondear números decimales. Además,
# demuestra cómo almacenar el resultado del redondeo en una
# variable y cómo especificar la cantidad de decimales que
# se desean conservar.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Redondeo de una operación matemática
# Se calcula el resultado de una división y se redondea al
# número entero más cercano.
# ------------------------------------------------------------

print(round(90 / 7))


# ------------------------------------------------------------
# Almacenamiento del resultado redondeado
# El resultado de la división se redondea y se guarda en una
# variable para utilizarlo posteriormente.
# ------------------------------------------------------------

resultado = round(80 / 7)

print(resultado)


# ------------------------------------------------------------
# Redondeo de un valor almacenado en una variable
# Primero se realiza la división y luego se redondea el
# resultado utilizando la función round().
# ------------------------------------------------------------

resultado1 = 100 / 7

redondeo = round(resultado1)

print(redondeo)


# ------------------------------------------------------------
# Redondeo con una cantidad específica de decimales
# ------------------------------------------------------------

valor = 95.66666666

# ------------------------------------------------------------
# Redondeo a dos decimales
# El segundo argumento de round() indica que el resultado
# debe conservar únicamente dos cifras decimales.
# ------------------------------------------------------------

print(round(valor, 2))


# ------------------------------------------------------------
# Redondeo a tres decimales
# El segundo argumento de round() indica que el resultado
# debe conservar únicamente tres cifras decimales.
# ------------------------------------------------------------

print(round(valor, 3))


# ------------------------------------------------------------
# Redondeo al número entero más cercano
# Cuando no se indica la cantidad de decimales, round()
# devuelve el entero más cercano.
# ------------------------------------------------------------

print(round(valor))


# ------------------------------------------------------------
# Verificación del tipo de dato
# Se muestra el tipo de dato de la variable original.
# ------------------------------------------------------------

print(type(valor))