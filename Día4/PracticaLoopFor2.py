# ------------------------------------------------------------
# Práctica Loop For 2
#
# Dada una lista de números, utiliza un loop For para realizar
# la suma de todos sus elementos.
#
# El resultado de la suma debe almacenarse en una variable
# llamada suma_numeros.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Crear la lista de números
#
# Se almacenan los números que serán recorridos y sumados
# posteriormente.
# ------------------------------------------------------------

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]


# ------------------------------------------------------------
# Crear la variable para almacenar la suma
#
# La variable suma_numeros comienza en 0 y se utilizará
# para acumular el valor de cada número de la lista.
# ------------------------------------------------------------

suma_numeros = 0


# ------------------------------------------------------------
# Recorrer la lista y sumar los números
#
# for recorre cada elemento de lista_numeros y almacena
# temporalmente cada número en la variable numero.
#
# += suma cada número al valor que ya contiene
# suma_numeros.
# ------------------------------------------------------------

for numero in lista_numeros:
    suma_numeros += numero  # Sumar cada número al total


# ------------------------------------------------------------
# Imprimir el resultado
#
# Se muestra el valor final almacenado en suma_numeros,
# que corresponde a la suma de todos los números de la lista.
# ------------------------------------------------------------

print(suma_numeros)