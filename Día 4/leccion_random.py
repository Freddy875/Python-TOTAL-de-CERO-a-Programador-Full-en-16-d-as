# ------------------------------------------------------------
# Importar funciones para generar valores aleatorios
# ------------------------------------------------------------

from random import *


# ------------------------------------------------------------
# randint()
# Genera un número entero aleatorio entre 1 y 50.
# Los valores 1 y 50 están incluidos.
# ------------------------------------------------------------

aleatorio = randint(1, 50)

# Imprime el número entero aleatorio generado.
print(aleatorio)


# ------------------------------------------------------------
# uniform()
# Genera un número decimal aleatorio entre 1 y 5.
# round() redondea el resultado a un decimal.
# ------------------------------------------------------------

aleatorio2 = round(uniform(1, 5), 1)

# Imprime el número decimal redondeado.
print(aleatorio2)


# ------------------------------------------------------------
# random()
# Genera un número decimal aleatorio entre 0 y 1.
# ------------------------------------------------------------

aleatorio3 = random()

# Imprime el número decimal aleatorio.
print(aleatorio3)


# ------------------------------------------------------------
# choice()
# Selecciona aleatoriamente un elemento de una lista.
# ------------------------------------------------------------

colores = ["azul", "verde", "rojo", "amarrillo"]

aleatorio4 = choice(colores)

# Imprime el color seleccionado aleatoriamente.
print(aleatorio4)


# ------------------------------------------------------------
# range()
# Genera números desde 5 hasta antes de 50,
# avanzando de 5 en 5.
# list() convierte el resultado en una lista.
# ------------------------------------------------------------

numeros = list(range(5, 50, 5))

print(numeros)


# ------------------------------------------------------------
# shuffle()
# Cambia aleatoriamente el orden de los elementos de la lista.
# Modifica directamente la lista original.
# ------------------------------------------------------------

shuffle(numeros)

# Imprime la lista después de cambiar aleatoriamente
# el orden de sus elementos.
print(numeros)