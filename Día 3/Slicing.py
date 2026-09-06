# ------------------------------------------------------------
# Este programa muestra diferentes formas de acceder a
# fragmentos de una cadena utilizando índices y slicing.
# Se utiliza el abecedario para observar cómo funcionan
# los índices, los rangos, los saltos y el orden inverso.
# ------------------------------------------------------------

abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


# ------------------------------------------------------------
# Acceder a un carácter mediante su índice
# El índice 2 obtiene el tercer carácter de la cadena,
# ya que Python comienza a contar desde el índice 0.
# ------------------------------------------------------------

fragmento = abecedario[2]

print(fragmento)


# ------------------------------------------------------------
# Obtener un fragmento entre dos índices
# [2:5] obtiene los caracteres desde el índice 2 hasta
# antes del índice 5.
# ------------------------------------------------------------

fragmento = abecedario[2:5]

print(fragmento)


# ------------------------------------------------------------
# Obtener un fragmento desde un índice hasta el final
# [2:] obtiene todos los caracteres desde el índice 2
# hasta el final de la cadena.
# ------------------------------------------------------------

fragmento = abecedario[2:]

print(fragmento)


# ------------------------------------------------------------
# Obtener un fragmento desde el inicio hasta un índice
# [:5] obtiene los caracteres desde el comienzo de la
# cadena hasta antes del índice 5.
# ------------------------------------------------------------

fragmento = abecedario[:5]

print(fragmento)


# ------------------------------------------------------------
# Obtener un fragmento utilizando un rango
# [2:10] obtiene los caracteres desde el índice 2 hasta
# antes del índice 10.
# ------------------------------------------------------------

fragmento = abecedario[2:10]

print(fragmento)


# ------------------------------------------------------------
# Obtener un fragmento utilizando un salto
# [2:10:2] obtiene los caracteres desde el índice 2 hasta
# antes del índice 10, avanzando de dos en dos posiciones.
# ------------------------------------------------------------

fragmento = abecedario[2:10:2]

print(fragmento)


# ------------------------------------------------------------
# Recorrer la cadena utilizando un salto
# [::3] recorre toda la cadena tomando un carácter cada
# tres posiciones.
# ------------------------------------------------------------

fragmento = abecedario[::3]

print(fragmento)


# ------------------------------------------------------------
# Obtener la cadena en orden inverso
# [::-1] recorre toda la cadena desde el final hasta el
# principio, invirtiendo su orden.
# ------------------------------------------------------------

fragmento = abecedario[::-1]

print(fragmento)