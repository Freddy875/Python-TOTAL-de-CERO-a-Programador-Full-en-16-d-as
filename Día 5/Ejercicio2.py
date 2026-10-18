# ------------------------------------------------------------
# Ejercicio 2
# Crear una función que reciba una palabra y devuelva sus
# letras únicas, sin repetir y en orden alfabético.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para obtener las letras únicas de una palabra.
# set() elimina las letras repetidas.
# sorted() ordena las letras alfabéticamente y devuelve una lista.
# ------------------------------------------------------------
def letras_unicas(palabra):
    letras = set(palabra)
    letras_ordenadas = sorted(letras)

    return letras_ordenadas


# ------------------------------------------------------------
# Solicitar una palabra al usuario.
# ------------------------------------------------------------
palabra = input("Ingresa una palabra: ")


# ------------------------------------------------------------
# Llamar a la función y mostrar el resultado.
# ------------------------------------------------------------
resultado = letras_unicas(palabra)

print(f"Las letras únicas en orden alfabético son: {resultado}")