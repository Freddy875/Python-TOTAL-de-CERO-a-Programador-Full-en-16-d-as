# ------------------------------------------------------------
# Comparación con doble signo igual
# El signo = se utiliza para asignar un valor a una variable.
# El signo == se utiliza para comparar dos valores.
# El resultado de una comparación siempre es un valor booleano:
# True o False.
# ------------------------------------------------------------

mi_variable = "Hola Mundo"


# ------------------------------------------------------------
# Comparar un string con otro string
# Se compara el contenido de mi_variable con "Hola Mundo".
# Como ambos valores son iguales, el resultado es True.
# ------------------------------------------------------------

mi_bool = mi_variable == "Hola Mundo"

print(type(mi_bool))
# Imprime: <class 'bool'>

print(mi_bool)
# Imprime: True


# ------------------------------------------------------------
# Comparación con un valor diferente
# Se compara mi_variable con "Hello World".
# Como los textos son diferentes, el resultado es False.
# ------------------------------------------------------------

mi_bool = mi_variable == "Hello World"

print(type(mi_bool))
# Imprime: <class 'bool'>

print(mi_bool)
# Imprime: False


# ------------------------------------------------------------
# Comparar un número con otro número
# Se comprueba si 10 es igual a 25.
# Como los valores son diferentes, el resultado es False.
# ------------------------------------------------------------

mi_numero = 10 == 25

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: False


# ------------------------------------------------------------
# Comparar una operación matemática
# Primero se realiza la operación 5 + 5.
# Después se compara el resultado con 10.
# Como ambos valores son iguales, el resultado es True.
# ------------------------------------------------------------

mi_numero = 10 == 5 + 5

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: True


# ------------------------------------------------------------
# Comparar dos strings
# Se comparan los textos "Blanco" y "Negro".
# Como son diferentes, el resultado es False.
# ------------------------------------------------------------

mi_string = "Blanco" == "Negro"

print(type(mi_string))
# Imprime: <class 'bool'>

print(mi_string)
# Imprime: False


# ------------------------------------------------------------
# Las comparaciones distinguen mayúsculas y minúsculas
# "blanco" y "Blanco" tienen diferente escritura,
# por lo que la comparación devuelve False.
# ------------------------------------------------------------

mi_string = "blanco" == "Blanco"

print(type(mi_string))
# Imprime: <class 'bool'>

print(mi_string)
# Imprime: False


# ------------------------------------------------------------
# Convertir un string a minúsculas antes de comparar
# El método lower() convierte "Blanco" en "blanco".
# Ahora ambos textos son iguales y el resultado es True.
# ------------------------------------------------------------

mi_string = "blanco" == "Blanco".lower()

print(type(mi_string))
# Imprime: <class 'bool'>

print(mi_string)
# Imprime: True


# ------------------------------------------------------------
# Comparar un número con un string
# Se compara el número entero 10 con el texto "10".
# Aunque representan el mismo valor visualmente, son de
# diferente tipo, por lo que la comparación devuelve False.
# ------------------------------------------------------------

mi_numero = 10 == "10"

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: False


# ------------------------------------------------------------
# Comparar un integer con un float
# Se compara 10 con 10.0.
# Aunque son tipos numéricos diferentes, representan el mismo
# valor, por lo que la comparación devuelve True.
# ------------------------------------------------------------

mi_numero = 10 == 10.0

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: True


# ------------------------------------------------------------
# Comparación diferente
# El operador != comprueba si dos valores son diferentes.
# Como 10 y 10.0 representan el mismo valor, devuelve False.
# ------------------------------------------------------------

mi_numero = 10 != 10.0

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: False


# ------------------------------------------------------------
# Comparación diferente con valores distintos
# Se comprueba si 10 es diferente de 9.99.
# Como los valores son diferentes, el resultado es True.
# ------------------------------------------------------------

mi_numero = 10 != 9.99

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: True


# ------------------------------------------------------------
# Símbolo mayor que
# El operador > comprueba si el valor de la izquierda
# es mayor que el valor de la derecha.
# ------------------------------------------------------------

mi_numero = 100 > 99

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: True


# ------------------------------------------------------------
# Símbolo menor que
# El operador < comprueba si el valor de la izquierda
# es menor que el valor de la derecha.
# ------------------------------------------------------------

mi_numero = 100 < 99

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: False


# ------------------------------------------------------------
# Símbolo mayor o igual que
# El operador >= comprueba si el valor de la izquierda
# es mayor o igual que el valor de la derecha.
# ------------------------------------------------------------

mi_numero = 100 >= 100

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: True


# ------------------------------------------------------------
# Símbolo menor o igual que
# El operador <= comprueba si el valor de la izquierda
# es menor o igual que el valor de la derecha.
# ------------------------------------------------------------

mi_numero = 100 <= 99

print(type(mi_numero))
# Imprime: <class 'bool'>

print(mi_numero)
# Imprime: False