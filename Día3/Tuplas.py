# ------------------------------------------------------------
# Tipo de dato tuple
# Se crea una tupla con varios números y type() permite
# comprobar el tipo de dato que contiene la variable.
# ------------------------------------------------------------

mi_tupla = (1, 2, 3, 4, 5)

print(type(mi_tupla))  # Imprime: <class 'tuple'>

print(mi_tupla)  # Imprime: (1, 2, 3, 4, 5)

# ------------------------------------------------------------
# Tupla con diferentes tipos de datos
# Una tupla puede almacenar strings, números decimales
# y valores booleanos, entre otros tipos de datos.
# ------------------------------------------------------------

otra_tupla = ("aaa", 3, 7.15, True)

print(otra_tupla)  # Imprime: ('aaa', 3, 7.15, True)


# ------------------------------------------------------------
# Acceder al primer elemento de una tupla
# El índice 0 corresponde al primer elemento.
# ------------------------------------------------------------

print(mi_tupla[0])  # Imprime: 1


# ------------------------------------------------------------
# Acceder a un elemento utilizando un índice negativo
# El índice -2 corresponde al penúltimo elemento de la tupla.
# ------------------------------------------------------------

print(mi_tupla[-2])  # Imprime: 4


# ------------------------------------------------------------
# Extraer una parte de la tupla mediante slicing
# Se obtienen los elementos desde el índice 1 hasta antes
# del índice 4.
# ------------------------------------------------------------

print(mi_tupla[1:4])  # Imprime: (2, 3, 4)


# ------------------------------------------------------------
# Slicing en una tupla de letras
# Se extraen los elementos desde el índice 1 hasta antes
# del índice 4.
# ------------------------------------------------------------

tupla_letras = ("a", "b", "c", "d", "e")

print(tupla_letras[1:4])  # Imprime: ('b', 'c', 'd')


# ------------------------------------------------------------
# Tuplas anidadas
# Una tupla puede contener otra tupla como uno de sus
# elementos.
# ------------------------------------------------------------

tupla_anidada = (1, 2, (3, 4), 5)

print(tupla_anidada)  # Imprime: (1, 2, (3, 4), 5)


# ------------------------------------------------------------
# Acceder a una tupla dentro de otra tupla
# El índice 2 permite obtener la tupla (3, 4).
# ------------------------------------------------------------

print(tupla_anidada[2])  # Imprime: (3, 4)


# ------------------------------------------------------------
# Acceder a un elemento dentro de una tupla anidada
# Primero se accede a la tupla interna con [2] y después
# al primer elemento de esa tupla con [0].
# ------------------------------------------------------------

print(tupla_anidada[2][0])  # Imprime: 3


# ------------------------------------------------------------
# Comprobar el tipo de dato antes de la conversión
# La variable contiene actualmente una tupla.
# ------------------------------------------------------------

print(type(tupla_anidada))  # Imprime: <class 'tuple'>


# ------------------------------------------------------------
# Convertir una tupla en una lista
# La función list() convierte la tupla y el resultado se
# reasigna a la misma variable.
# ------------------------------------------------------------

tupla_anidada = list(tupla_anidada)

print(tupla_anidada)  # Imprime: [1, 2, (3, 4), 5]

print(type(tupla_anidada))  # Imprime: <class 'list'>


# ------------------------------------------------------------
# Lista que será convertida en una tupla
# Primero se comprueba que la variable contiene una lista.
# ------------------------------------------------------------

mi_lista = ["a", "b", "c", "d", "e"]

print(type(mi_lista))  # Imprime: <class 'list'>


# ------------------------------------------------------------
# Convertir una lista en una tupla
# La función tuple() convierte la lista y el resultado se
# reasigna a la misma variable.
# ------------------------------------------------------------

mi_lista = tuple(mi_lista)

print(mi_lista)  # Imprime: ('a', 'b', 'c', 'd', 'e')

print(type(mi_lista))  # Imprime: <class 'tuple'>


# ------------------------------------------------------------
# Desempacar una tupla en variables
# Cada elemento de la tupla se asigna a una variable.
# Debe existir la misma cantidad de variables y elementos.
# ------------------------------------------------------------

tupla_numeros = (1, 2, 3)

x, y, z = tupla_numeros

print(x, y, z)  # Imprime: 1 2 3


# ------------------------------------------------------------
# Longitud de una tupla
# La función len() devuelve la cantidad de elementos que
# contiene la tupla.
# ------------------------------------------------------------

tupla_colores = ("rojo", "verde", "azul")

print(tupla_colores)  # Imprime: ('rojo', 'verde', 'azul')

print(len(tupla_colores))  # Imprime: 3

# ------------------------------------------------------------
# Método count()
# count() cuenta cuántas veces aparece el número 2 dentro
# de la tupla.
# ------------------------------------------------------------

numeros = (1, 2, 2, 3, 2, 4, 2, 5, 2)

print(numeros.count(2))  # Imprime: 5


# ------------------------------------------------------------
# Tupla con números repetidos
# Esta tupla contiene varios números, incluyendo números
# repetidos y el número 3.
# ------------------------------------------------------------

numeros = (1, 2, 2, 5, 2, 5, 4, 2, 5, 2, 3)


# ------------------------------------------------------------
# Método count() dentro de un mensaje
# Cuenta cuántas veces aparece el número 2 y muestra el
# resultado directamente mediante un f-string.
# ------------------------------------------------------------

print(f"El número 2 apareció {numeros.count(2)} veces")
# Imprime: El número 2 apareció 5 veces


# ------------------------------------------------------------
# Método index()
# Busca la posición de la primera aparición del número 3
# y muestra el resultado directamente dentro del mensaje.
# ------------------------------------------------------------

print(f"El número 3 se encuentra en la posición {numeros.index(3)}")
# Imprime: El número 3 se encuentra en la posición 10

# ------------------------------------------------------------
# Desempacar una tupla en variables
# Cada elemento de la tupla se asigna a una variable.
# Aunque la tupla es inmutable, las variables creadas pueden
# recibir nuevos valores sin modificar la tupla original.
# ------------------------------------------------------------

tupla_letras = ("a", "b", "c", "d", "e")

x, y, z = tupla_letras[0], tupla_letras[1], tupla_letras[2]

print(x.upper(), y, z)  # Imprime: A b c