# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (*args) 3
# Crear una función que reciba un nombre y una cantidad
# indeterminada de números, y devuelva la suma en un mensaje.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para sumar los números de una persona
# nombre recibe el nombre como primer argumento.
# *numeros recibe una cantidad variable de números.
# sum() calcula la suma de todos los números recibidos.
# El f-string construye el mensaje con el nombre y la suma.
# ------------------------------------------------------------
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


# ------------------------------------------------------------
# No se invoca la función, según la consigna.
# ------------------------------------------------------------