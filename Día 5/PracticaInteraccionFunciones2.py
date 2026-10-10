# ------------------------------------------------------------
# Funciones 2
# Crear una función llamada reducir_lista que reciba una lista,
# elimine los elementos duplicados y elimine el valor más alto.
# Crear otra función llamada promedio que reciba la lista
# reducida y devuelva el promedio de sus valores.
# También se debe crear la variable lista_numeros.
# No se deben invocar las funciones.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función reducir_lista
# Recibe una lista como argumento.
# set() elimina los elementos duplicados.
# list() convierte el conjunto nuevamente en una lista.
# max() identifica el valor más alto y remove() lo elimina.
# return devuelve la lista reducida.
# ------------------------------------------------------------

def reducir_lista(lista):
    lista_unica = list(set(lista))  # Convertir a set para eliminar duplicados y luego volver a lista
    lista_unica.remove(max(lista_unica))  # Eliminar el número más alto
    return lista_unica  # Retornar la lista reducida


# ------------------------------------------------------------
# Definir la función promedio
# Recibe una lista como argumento.
# sum() suma sus valores y len() cuenta sus elementos.
# Se divide la suma entre la cantidad de elementos para
# calcular el promedio.
# Si la lista está vacía, devuelve 0 para evitar la
# división entre cero.
# ------------------------------------------------------------

def promedio(lista):
    return sum(lista) / len(lista) if lista else 0  # Evitar división por cero si la lista está vacía


# ------------------------------------------------------------
# Crear la lista de números
# Se almacena una lista que contiene números repetidos
# para probar posteriormente la función reducir_lista.
# ------------------------------------------------------------

lista_numeros = [1, 2, 15, 7, 2]


# ------------------------------------------------------------
# No invocar las funciones
# La práctica solicita definir las dos funciones y crear
# la lista, sin ejecutarlas todavía.
# ------------------------------------------------------------