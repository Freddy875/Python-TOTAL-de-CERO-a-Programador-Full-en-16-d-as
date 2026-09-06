# ------------------------------------------------------------
# Este programa utiliza slicing para invertir la posición de
# todos los caracteres de una frase.
#
# Se utiliza [::-1], que recorre la cadena desde el final
# hasta el principio, avanzando una posición hacia atrás
# en cada paso.
# ------------------------------------------------------------

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

frase_invertida = frase[::-1]

print(frase_invertida)