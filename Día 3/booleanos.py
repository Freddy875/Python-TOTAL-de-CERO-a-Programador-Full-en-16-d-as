# ------------------------------------------------------------
# Variables booleanas
# Se crean dos variables y se les asignan directamente los
# valores booleanos True y False.
# ------------------------------------------------------------

var1 = True

var2 = False


# ------------------------------------------------------------
# Comprobar el tipo de dato y mostrar el valor
# La función type() permite conocer el tipo de dato de var1
# y print() muestra su valor.
# ------------------------------------------------------------

print(type(var1))  # Imprime: <class 'bool'>

print(var1)  # Imprime: True


# ------------------------------------------------------------
# Crear un valor booleano mediante una comparación
# Se pregunta si el número 5 es mayor que 5.
# Como ambos valores son iguales, el resultado es False.
# ------------------------------------------------------------

numero = 5 > 5

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: False


# ------------------------------------------------------------
# Comparar si un número es menor que otro
# Se pregunta si el número 5 es menor que 5.
# Como ambos valores son iguales, el resultado es False.
# ------------------------------------------------------------

numero = 5 < 5

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: False


# ------------------------------------------------------------
# Comparar si dos valores son iguales
# El operador == comprueba si ambos valores son iguales.
# En este caso, el resultado es True.
# ------------------------------------------------------------

numero = 5 == 5

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: True


# ------------------------------------------------------------
# Comparar si un número es mayor o igual que otro
# El operador >= comprueba si el primer valor es mayor o
# igual que el segundo valor.
# ------------------------------------------------------------

numero = 5 >= 5

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: True


# ------------------------------------------------------------
# Comparar si un número es menor o igual que otro
# El operador <= comprueba si el primer valor es menor o
# igual que el segundo valor.
# ------------------------------------------------------------

numero = 5 <= 5

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: True


# ------------------------------------------------------------
# Comparar si dos valores son diferentes
# El operador != comprueba si ambos valores son distintos.
# En este caso, 5 es diferente de 3, por lo tanto el
# resultado es True.
# ------------------------------------------------------------

numero = 5 != 3

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: True


# ------------------------------------------------------------
# Convertir el resultado de una comparación a booleano
# La función bool() devuelve un valor booleano a partir del
# resultado de la comparación.
# ------------------------------------------------------------

numero = bool(5 != 3)

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: True


# ------------------------------------------------------------
# Generar un valor booleano False
# Al utilizar bool() sin proporcionar un valor, Python
# devuelve False.
# ------------------------------------------------------------

numero = bool()

print(type(numero))  # Imprime: <class 'bool'>

print(numero)  # Imprime: False


# ------------------------------------------------------------
# Consultar si un elemento se encuentra en una lista
# El operador in comprueba si el número 5 está dentro de
# la lista y devuelve un valor booleano.
# ------------------------------------------------------------

lista = [1, 2, 3, 4, 5]

control = 5 in lista

print(type(control))  # Imprime: <class 'bool'>

print(control)  # Imprime: True


# ------------------------------------------------------------
# Consultar directamente si un elemento está en una lista
# El operador in devuelve True si encuentra el elemento
# dentro de la lista.
# ------------------------------------------------------------

lista = [1, 2, 3, 4, 5]

print(3 in lista)  # Imprime: True


# ------------------------------------------------------------
# Comprobar mediante una negación si un elemento no está
# dentro de una lista.
# El operador not in devuelve True cuando el elemento no
# se encuentra en la lista.
# ------------------------------------------------------------

lista = [1, 2, 3, 4, 5]

print(6 not in lista)  