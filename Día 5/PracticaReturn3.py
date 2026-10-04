# ------------------------------------------------------------
# Práctica Return 3
# Crear una función llamada invertir_palabra que reciba una
# palabra como argumento, invierta el orden de sus caracteres
# y la devuelva en mayúsculas.
# También se debe crear una variable llamada palabra y
# utilizarla como argumento de la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función para invertir una palabra y convertirla
# a mayúsculas.
# [::-1] invierte el orden de los caracteres.
# .upper() convierte todos los caracteres a mayúsculas.
# return devuelve la palabra modificada.
# ------------------------------------------------------------

def invertir_palabra(palabra):
    return palabra[::-1].upper()  # Invierte la palabra y la convierte en mayúsculas


# ------------------------------------------------------------
# Crear una variable con una palabra
# Se almacena "Python" en la variable palabra.
# ------------------------------------------------------------

palabra = "Python"  # Puedes cambiarla por cualquier otra


# ------------------------------------------------------------
# Llamar a la función y obtener el resultado
# Se envía la variable palabra como argumento a la función.
# El resultado que devuelve return se guarda en resultado.
# ------------------------------------------------------------

resultado = invertir_palabra(palabra)


# ------------------------------------------------------------
# Imprimir el resultado
# Se muestra en pantalla la palabra invertida y en mayúsculas.
# ------------------------------------------------------------

print(resultado)