# ------------------------------------------------------------
# Este programa muestra diferentes formas de acceder a
# caracteres y buscar texto dentro de una cadena utilizando
# índices y los métodos index() y rindex().
# ------------------------------------------------------------

mi_texto = "Esta es una prueba"


# ------------------------------------------------------------
# Acceder a un carácter mediante un índice
# El índice 0 corresponde al primer carácter de la cadena.
# ------------------------------------------------------------

resultado = mi_texto[0]

print(resultado)


# ------------------------------------------------------------
# Acceder a un carácter utilizando un índice negativo
# El índice -4 cuenta los caracteres desde el final de
# la cadena.
# ------------------------------------------------------------

resultado = mi_texto[-4]

print(resultado)


# ------------------------------------------------------------
# Buscar la posición de un carácter
# El método index() devuelve la posición en la que aparece
# por primera vez el carácter indicado.
# ------------------------------------------------------------

resultado = mi_texto.index("n")

print(resultado)


# ------------------------------------------------------------
# Buscar la posición de un texto
# index() también permite encontrar la posición donde
# comienza una palabra o una parte de la cadena.
# ------------------------------------------------------------

resultado = mi_texto.index("prueba")

print(resultado)


# ------------------------------------------------------------
# Buscar la primera aparición de un carácter
# index() devuelve la posición de la primera "a" encontrada
# dentro de la cadena.
# ------------------------------------------------------------

resultado = mi_texto.index("a")

print(resultado)


# ------------------------------------------------------------
# Buscar un carácter comenzando desde una posición
# El segundo argumento de index() indica desde qué posición
# debe comenzar la búsqueda.
# ------------------------------------------------------------

resultado = mi_texto.index("a", 5)

print(resultado)


# ------------------------------------------------------------
# Buscar un carácter dentro de un rango
# El segundo argumento indica dónde comienza la búsqueda y
# el tercero indica dónde termina el rango de búsqueda.
# ------------------------------------------------------------

resultado = mi_texto.index("a", 5, 11)

print(resultado)


# ------------------------------------------------------------
# Buscar desde el final de la cadena
# El método rindex() busca la última aparición del carácter
# indicado y devuelve su posición.
# ------------------------------------------------------------

resultado = mi_texto.rindex("a")

print(resultado)