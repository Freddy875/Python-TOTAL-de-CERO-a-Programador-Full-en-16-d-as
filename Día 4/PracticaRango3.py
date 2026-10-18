# ------------------------------------------------------------
# Práctica Rango 3
#
# Utiliza la función range() y un loop para sumar los cuadrados
# de todos los números del 1 al 15, incluyendo ambos valores.
#
# El resultado de la suma debe almacenarse en la variable
# suma_cuadrados.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Inicializar la variable para la suma
#
# La variable suma_cuadrados comienza en 0 y se utilizará
# para acumular el cuadrado de cada número.
# ------------------------------------------------------------

suma_cuadrados = 0


# ------------------------------------------------------------
# Recorrer el rango de 1 a 15
#
# range(1, 16) genera los números desde 1 hasta 15,
# ya que el segundo valor no se incluye.
#
# for recorre cada número y lo almacena temporalmente
# en la variable num.
#
# ** 2 eleva cada número al cuadrado.
#
# += acumula cada cuadrado en la variable suma_cuadrados.
# ------------------------------------------------------------

for numero in range(1, 16):
    suma_cuadrados += numero ** 2  # Elevar al cuadrado y sumar al acumulador


# ------------------------------------------------------------
# Imprimir el resultado
#
# Se muestra el valor final almacenado en suma_cuadrados,
# que corresponde a la suma de los cuadrados de los números
# del 1 al 15.
# ------------------------------------------------------------

print(suma_cuadrados)