# ------------------------------------------------------------
# Tipo de dato de una lista numérica
# type() permite comprobar que la variable contiene una lista.
# ------------------------------------------------------------

lista_numerica = [1, 2, 3, 4, 5]

print(type(lista_numerica))


# ------------------------------------------------------------
# Tipo de dato de una lista de strings
# Las listas pueden contener diferentes tipos de datos.
# ------------------------------------------------------------

lista = ["a", "b", "c"]

print(type(lista))


# ------------------------------------------------------------
# Longitud de una lista
# len() devuelve la cantidad de elementos que contiene
# la lista.
# ------------------------------------------------------------

mi_lista = ["Hola", 30, 40, 600]

print(len(mi_lista))


# ------------------------------------------------------------
# Indexar el contenido de una lista
# Los índices permiten acceder a elementos específicos.
# El índice 2 corresponde al tercer elemento de la lista.
# ------------------------------------------------------------

print(lista_numerica[2])


# ------------------------------------------------------------
# Mostrar la lista al revés
# El slicing [::-1] permite recorrer la lista desde el
# último elemento hasta el primero.
# ------------------------------------------------------------

print(lista_numerica[::-1])


# ------------------------------------------------------------
# Concatenar listas
# El operador + permite unir dos listas en una sola.
# ------------------------------------------------------------

mi_otra_lista = [6, 7, 8]

print(lista_numerica + mi_otra_lista)


# ------------------------------------------------------------
# Guardar una lista concatenada
# El resultado de unir las dos listas se almacena en una
# nueva variable.
# ------------------------------------------------------------

mi_gran_lista = lista_numerica + mi_otra_lista

print(mi_gran_lista)


# ------------------------------------------------------------
# Modificar el contenido de una lista
# Las listas son mutables, por lo que podemos cambiar
# directamente el valor de uno de sus elementos utilizando
# su índice.
# ------------------------------------------------------------

mi_gran_lista[0] = "uno"

print(mi_gran_lista)


# ------------------------------------------------------------
# Método append()
# append() agrega un nuevo elemento al final de la lista.
# ------------------------------------------------------------

mi_gran_lista[0] = 1

mi_gran_lista.append(9)

print(mi_gran_lista)


# ------------------------------------------------------------
# Método pop()
# pop() elimina el último elemento de la lista cuando no se
# indica ningún índice.
# ------------------------------------------------------------

mi_gran_lista.pop()

print(mi_gran_lista)


# ------------------------------------------------------------
# Método pop() almacenando el elemento eliminado
# Al indicar un índice, pop() elimina el elemento que ocupa
# esa posición y permite guardar el elemento eliminado en
# una variable para utilizarlo posteriormente.
# ------------------------------------------------------------

elemento_eliminado = mi_gran_lista.pop(2)

print(mi_gran_lista)
print(elemento_eliminado)


# ------------------------------------------------------------
# Método sort() con strings
# sort() organiza los elementos de una lista en orden
# alfabético.
# ------------------------------------------------------------

lista_alfabetica = ["G", "E", "C", "D", "F", "B", "A"]

lista_alfabetica.sort()

print(lista_alfabetica)


# ------------------------------------------------------------
# Método sort() con números
# sort() también permite organizar los números de menor
# a mayor.
# ------------------------------------------------------------

otra_lista_numerica = [6, 3, 2, 4, 5, 1]

otra_lista_numerica.sort()

print(otra_lista_numerica)


# ------------------------------------------------------------
# Método reverse()
# reverse() invierte el orden actual de los elementos de
# la lista.
# ------------------------------------------------------------

otra_lista_alfabetica = ["G", "F", "E", "D", "C", "B", "A"]

otra_lista_alfabetica.reverse()

print(otra_lista_alfabetica)