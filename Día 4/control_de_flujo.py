# ------------------------------------------------------------
# Condición verdadera
#
# Se utiliza una condición directamente con el valor True.
# Como la condición es verdadera, se ejecuta el bloque del if.
# Si fuera False, se ejecutaría el bloque del else.
# ------------------------------------------------------------

if True:
    print("Condición verdadera")
else:
    print("Condición falsa")


# ------------------------------------------------------------
# Comparación con if
#
# Se comprueba si 10 es mayor que 9.
# Como la condición es verdadera, se ejecuta el print.
# ------------------------------------------------------------

if 10 > 9:
    print("Es correcto 10 es mayor que 9")


# ------------------------------------------------------------
# Condición que nunca se cumple
#
# Se comprueba si 10 es mayor que 99.
# Esta condición es falsa, por lo que el bloque del if
# no se ejecuta.
# ------------------------------------------------------------

if 10 > 99:
    print("Es correcto 10 es mayor que 9")


# ------------------------------------------------------------
# Uso de if y else
#
# Se almacena el valor 3 en la variable x.
# Después se comprueba si x es mayor que 100.
# Como la condición es falsa, se ejecuta el bloque del else.
# ------------------------------------------------------------

x = 3

if x > 100:
    print("Es correcto")
else:
    print("Es incorrecto")


# ------------------------------------------------------------
# Determinar el tipo de mascota
#
# Se almacena el tipo de mascota en la variable mascota.
# Se utiliza if, elif y else para comprobar diferentes
# posibilidades y mostrar un mensaje según el valor.
# ------------------------------------------------------------

mascota = "gato"

if mascota == "perro":
    print("Tienes un perro")
elif mascota == "canario":
    print("Tienes un canario")
elif mascota == "hamster":
    print("Tienes un hamster")
elif mascota == "gato":
    print("Tienes un gato")
elif mascota == "pez":
    print("Tienes un pez")
elif mascota == "conejo":
    print("Tienes un conejo")
else:
    print("No se que tipo de mascota tienes")