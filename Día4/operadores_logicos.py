# ------------------------------------------------------------
# Comparar operadores lógicos
# Los operadores lógicos permiten combinar o invertir
# condiciones y obtener un resultado booleano: True o False.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Comparación encadenada
# Python permite realizar varias comparaciones en una misma
# expresión.
# En este caso, comprueba que 4 sea menor que 5 y que 5
# sea menor que 6.
# ------------------------------------------------------------

mi_bool = 4 < 5 < 6

print(mi_bool)
# Imprime: True


# ------------------------------------------------------------
# Comparación encadenada con diferentes condiciones
# Se comprueba que 4 sea menor que 5 y que 5 sea mayor que 6.
# La primera condición es verdadera, pero la segunda es falsa.
# ------------------------------------------------------------

mi_bool = 4 < 5 > 6

print(mi_bool)
# Imprime: False


# ------------------------------------------------------------
# Operador lógico AND
# El operador and devuelve True solamente cuando ambas
# condiciones son verdaderas.
# ------------------------------------------------------------

mi_bool = 4 < 5 and 5 < 6

print(mi_bool)
# Imprime: True


# ------------------------------------------------------------
# Combinar condiciones con paréntesis
# Los paréntesis permiten separar y hacer más claras
# las condiciones que se están comparando.
# ------------------------------------------------------------

mi_bool = (4 < 5) and (5 == 2 * 3)

print(mi_bool)
# Imprime: False


# ------------------------------------------------------------
# AND con diferentes tipos de datos
# Se comprueba si 55 es igual a 55 y si "gato" es igual
# a "gato".
# Como ambas condiciones son verdaderas, el resultado es True.
# ------------------------------------------------------------

mi_bool = (55 == 55) and ("gato" == "gato")

print(mi_bool)
# Imprime: True


# ------------------------------------------------------------
# Operador lógico OR
# El operador or devuelve True cuando al menos una de las
# condiciones es verdadera.
# ------------------------------------------------------------

mi_bool = 10 == 5 or 3 < 6

print(mi_bool)
# Imprime: True


# ------------------------------------------------------------
# OR cuando ninguna condición es verdadera
# Se comprueba si 10 es igual a 5 o si 3 es igual a 6.
# Como ninguna de las dos condiciones se cumple, el resultado
# es False.
# ------------------------------------------------------------

mi_bool = 10 == 5 or 3 == 6

print(mi_bool)
# Imprime: False


# ------------------------------------------------------------
# Comparar texto con AND
# El operador in comprueba si una palabra se encuentra
# dentro de un texto.
# Como ambas palabras están en el texto, el resultado es True.
# ------------------------------------------------------------

texto = "Esta frase es breve"

mi_bool = "frase" in texto and "breve" in texto

print(mi_bool)
# Imprime: True


# ------------------------------------------------------------
# Comparar texto con AND cuando una condición es falsa
# "frase" se encuentra en el texto, pero "Hola" no.
# Como and necesita que ambas condiciones sean verdaderas,
# el resultado es False.
# ------------------------------------------------------------

mi_bool = "frase" in texto and "Hola" in texto

print(mi_bool)
# Imprime: False


# ------------------------------------------------------------
# Comparar texto con OR
# Se comprueba si "frase" o "Hola" se encuentran en el texto.
# Como "frase" sí se encuentra, el resultado es True.
# ------------------------------------------------------------

mi_bool = "frase" in texto or "Hola" in texto

print(mi_bool)
# Imprime: True


# ------------------------------------------------------------
# Operador NOT
# El operador not invierte el resultado de una condición.
# Si la condición es True, not la convierte en False.
# ------------------------------------------------------------

mi_bool = not ("a" == "a")

print(mi_bool)
# Imprime: False


# ------------------------------------------------------------
# NOT con una comparación diferente
# La condición "a" != "a" es False porque ambos valores
# son iguales.
# El operador not invierte ese resultado y lo convierte en True.
# ------------------------------------------------------------

mi_bool = not ("a" != "a")

print(mi_bool)
# Imprime: True