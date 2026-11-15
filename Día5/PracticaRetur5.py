# ------------------------------------------------------------
# Práctica Return 5
# Crear una función llamada invertir_palabra que reciba una
# palabra como argumento, invierta el orden de sus caracteres
# y la devuelva en mayúsculas.
# Pedir una palabra al usuario y utilizarla como argumento
# de la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función para invertir una palabra y convertirla
# a mayúsculas.
# [::-1] invierte el orden de los caracteres.
# .upper() convierte los caracteres a mayúsculas.
# return devuelve la palabra modificada.
# ------------------------------------------------------------

def invertir_palabra(palabra):
    return palabra[::-1].upper()


# ------------------------------------------------------------
# Pedir una palabra al usuario
# La palabra ingresada se almacena en la variable palabra.
# ------------------------------------------------------------

palabra = input("Ingresa una palabra: ")


# ------------------------------------------------------------
# Llamar a la función y obtener el resultado
# Se envía la palabra ingresada como argumento.
# El resultado que devuelve return se guarda en resultado.
# ------------------------------------------------------------

resultado = invertir_palabra(palabra)


# ------------------------------------------------------------
# Mostrar el resultado
# Se imprime la palabra invertida y en mayúsculas.
# ------------------------------------------------------------

print(f"La palabra invertida es: {resultado}")