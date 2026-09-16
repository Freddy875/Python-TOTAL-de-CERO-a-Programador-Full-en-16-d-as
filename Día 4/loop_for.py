# ------------------------------------------------------------
# Crear una lista de nombres
#
# Se almacenan los nombres de las personas dentro de una lista.
# ------------------------------------------------------------

nombres = ["Juan", "Ana", "Carlos", "Belen", "Fran"]


# ------------------------------------------------------------
# Recorrer la lista
#
# for recorre cada elemento de la lista y almacena
# temporalmente cada nombre en la variable nombre.
# ------------------------------------------------------------

for nombre in nombres:
    print(f"Hola {nombre}")


# ------------------------------------------------------------
# Crear una lista de letras
#
# Se almacenan diferentes letras dentro de una lista.
# ------------------------------------------------------------

mi_lista = ["a", "b", "c"]


# ------------------------------------------------------------
# Recorrer la lista
#
# for recorre cada elemento de mi_lista y lo almacena
# temporalmente en la variable letra.
# ------------------------------------------------------------

for letra in mi_lista:
    print(f"Elemento: {letra}")


# ------------------------------------------------------------
# Agregar un elemento a la lista
#
# append() agrega el elemento "d" al final de mi_lista.
# ------------------------------------------------------------

print("Agregar un elemento a la lista")

mi_lista.append("d")


# ------------------------------------------------------------
# Obtener el índice de cada elemento
#
# for recorre cada elemento de la lista.
#
# index() obtiene la posición que ocupa cada elemento
# dentro de mi_lista y la almacena en numero_letra.
# ------------------------------------------------------------

for letra in mi_lista:
    numero_letra = mi_lista.index(letra)
    print(f"La letra: {letra} tiene el indice {numero_letra}")


# ------------------------------------------------------------
# Agregar varios elementos a la lista de nombres
#
# extend() agrega varios elementos al final de la lista
# de una sola vez.
# ------------------------------------------------------------

nombres.extend(["Luis", "Pablo", "Laura", "Julia"])


# ------------------------------------------------------------
# Comprobar el tipo de dato
#
# type() permite conocer el tipo de dato que contiene
# la variable nombres.
# ------------------------------------------------------------

print(type(nombres))


# ------------------------------------------------------------
# Imprimir nombres que empiezan con L
#
# for recorre cada nombre de la lista.
#
# startswith() comprueba si el nombre comienza con la letra L.
#
# if ejecuta el print correspondiente cuando la condición
# se cumple.
#
# else se ejecuta cuando el nombre no comienza con L.
# ------------------------------------------------------------

for nombre in nombres:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print(f"Este nombre {nombre} no comienza con L")


# ------------------------------------------------------------
# Crear una lista de números
#
# Se almacenan los números del 1 al 5 dentro de una lista.
# ------------------------------------------------------------

numeros = [1, 2, 3, 4, 5]


# ------------------------------------------------------------
# Crear una variable para acumular valores
#
# valor comienza en 0 y posteriormente se utilizará
# para acumular la suma de los números.
# ------------------------------------------------------------

valor = 0


# ------------------------------------------------------------
# Sumar los elementos de la lista
#
# for recorre cada número de la lista.
#
# En cada vuelta, el número actual se suma al valor
# acumulado anteriormente.
# ------------------------------------------------------------

for numero in numeros:
    valor = valor + numero


# ------------------------------------------------------------
# Mostrar el resultado de la suma
#
# Se imprime el valor acumulado después de recorrer
# todos los elementos de la lista.
# ------------------------------------------------------------

print(valor)


# ------------------------------------------------------------
# Crear una cadena de texto
#
# Se almacena una frase dentro de la variable palabra.
# ------------------------------------------------------------

palabra = "python es genial"


# ------------------------------------------------------------
# Imprimir un espacio en blanco
#
# \n representa un salto de línea y permite dejar
# un espacio antes de mostrar los siguientes resultados.
# ------------------------------------------------------------

print("\n")


# ------------------------------------------------------------
# Recorrer una cadena de texto
#
# for recorre cada carácter de la cadena de texto.
# En cada vuelta, letra contiene un carácter diferente.
# ------------------------------------------------------------

for letra in palabra:
    print(letra)


# ------------------------------------------------------------
# Desempaquetar elementos de una lista de listas
#
# Cada elemento de la lista contiene dos valores.
# for desempaqueta esos valores y los almacena en
# las variables a y b.
# ------------------------------------------------------------

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)


# ------------------------------------------------------------
# Imprimir un espacio en blanco
#
# \n representa un salto de línea y permite separar
# el resultado anterior del siguiente ejemplo.
# ------------------------------------------------------------

print("\n")


# ------------------------------------------------------------
# Crear un diccionario de libros
#
# Se almacenan números como claves y nombres de libros
# como valores.
# ------------------------------------------------------------

libros = {
    1: "El principito",
    2: "Don Quijote de la Mancha",
    3: "Cien años de soledad",
    4: "Orgullo y prejuicio",
    5: "Crimen y castigo"
}


# ------------------------------------------------------------
# Recorrer el diccionario
#
# items() permite obtener la clave y el valor de cada
# elemento del diccionario.
#
# for desempaqueta cada par en las variables a y b:
# a recibe la clave y b recibe el valor.
# ------------------------------------------------------------

for a, b in libros.items():
    print(a)
    print(b)