# ------------------------------------------------------------
# Recorrer una lista con for
#
# Se crea una lista con los números del 1 al 5.
# for recorre cada elemento de la lista y lo almacena
# temporalmente en la variable numero.
# ------------------------------------------------------------

lista_numerica = [1, 2, 3, 4, 5]

for numero in lista_numerica:
    print(numero)


# ------------------------------------------------------------
# range() con un solo valor
#
# Cuando range() recibe un solo valor, ese valor indica
# hasta dónde llega el rango, sin incluirlo.
#
# El conteo comienza desde 0 si no se especifica un inicio.
#
# range(5) genera los valores del 0 al 4.
# ------------------------------------------------------------

print("\n")

for numero in range(5):
    print(numero)


# ------------------------------------------------------------
# range() indicando inicio y final
#
# El primer valor indica dónde comienza el rango.
# El segundo valor indica dónde termina, sin incluirlo.
#
# range(10, 21) genera los números del 10 al 20.
# ------------------------------------------------------------

for numero in range(10, 21):
    print(numero)


# ------------------------------------------------------------
# range() con un tercer valor: los pasos
#
# El tercer valor indica de cuánto en cuánto avanza el rango.
#
# En este caso, el rango comienza en 10, termina antes de 21
# y avanza de 3 en 3.
# ------------------------------------------------------------

print("\n")

for numero in range(10, 21, 3):
    print(numero)


# ------------------------------------------------------------
# Crear una lista utilizando range()
#
# range(1, 101) genera los números desde 1 hasta 100.
#
# list() convierte el rango generado en una lista.
# El resultado se almacena en mi_lista.
# ------------------------------------------------------------

mi_lista = list(range(1, 101))

print(mi_lista)