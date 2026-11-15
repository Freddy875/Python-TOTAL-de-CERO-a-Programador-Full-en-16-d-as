# ------------------------------------------------------------
# Práctica Interrupción de Flujo
#
# Crea un loop For que recorra la lista de números e imprima
# cada uno de sus elementos.
#
# El loop debe interrumpirse en el momento en que encuentre
# un valor negativo.
#
# No se debe cambiar el orden de la lista.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Crear la lista de números
#
# Se almacenan los números que serán recorridos por el loop.
# La lista contiene valores positivos y, posteriormente,
# valores negativos.
# ------------------------------------------------------------

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]


# ------------------------------------------------------------
# Recorrer la lista
#
# for recorre cada elemento de lista_numeros y almacena
# temporalmente cada valor en la variable numero.
#
# if comprueba si el número es menor que 0.
#
# Si encuentra un número negativo, break interrumpe
# completamente el loop.
#
# Los números se imprimen solamente cuando no se ha encontrado
# un valor negativo.
# ------------------------------------------------------------

for numero in lista_numeros:

    if numero < 0:  # Verificar si el número es negativo
        break  # Interrumpir el loop

    print(numero)