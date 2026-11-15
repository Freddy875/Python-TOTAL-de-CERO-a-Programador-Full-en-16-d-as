# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crear una función que devuelva en una lista los valores
# de los atributos recibidos como argumentos nombrados.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para obtener los valores de los atributos
# **kwargs recibe una cantidad indeterminada de argumentos
# nombrados y los reúne en un diccionario.
# values() obtiene los valores del diccionario.
# list() convierte esos valores en una lista.
# ------------------------------------------------------------
def lista_atributos(**kwargs):
    return list(kwargs.values())


# ------------------------------------------------------------
# Ejemplos de uso de la función
# Se muestran los valores de los argumentos recibidos.
# ------------------------------------------------------------
print(lista_atributos(nombre="Carlos", edad=25, ciudad="Madrid"))
# Imprime: ['Carlos', 25, 'Madrid']

print(lista_atributos(a=10, b=20, c=30))
# Imprime: [10, 20, 30]

print(lista_atributos())
# Imprime: []
