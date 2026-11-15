# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crear una función que cuente cuántos argumentos nombrados
# recibe y devuelva esa cantidad.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para contar los atributos recibidos
# **kwargs permite recibir una cantidad indefinida de argumentos
# nombrados y los reúne en un diccionario.
# len() devuelve la cantidad de claves del diccionario.
# ------------------------------------------------------------
def cantidad_atributos(**kwargs):
    return len(kwargs)


# ------------------------------------------------------------
# Ejemplos de uso de la función
# Cada argumento nombrado cuenta como un atributo.
# ------------------------------------------------------------
print(cantidad_atributos(nombre="Juan", edad=30, ciudad="Madrid"))  # Imprime: 3
print(cantidad_atributos(a=1, b=2))  # Imprime: 2
print(cantidad_atributos())  # Imprime: 0
