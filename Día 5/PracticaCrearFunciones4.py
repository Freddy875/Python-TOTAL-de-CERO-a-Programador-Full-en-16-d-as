# ------------------------------------------------------------
# Práctica Crear Funciones 4
# Crear una función llamada bienvenida que reciba como
# argumento el nombre de una persona e imprima un saludo.
# Pedir el nombre al usuario y llamar a la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función bienvenida
# Recibe el nombre de la persona como argumento y muestra
# un mensaje de bienvenida.
# ------------------------------------------------------------

def bienvenida(nombre_persona):
    print(f"¡Bienvenid@ {nombre_persona}!")


# ------------------------------------------------------------
# Pedir el nombre al usuario
# El nombre ingresado se guarda en la variable nombre_persona.
# ------------------------------------------------------------

nombre_persona = input("¿Cuál es tu nombre? ")


# ------------------------------------------------------------
# Llamar a la función
# Se envía el nombre ingresado por el usuario como argumento.
# ------------------------------------------------------------

bienvenida(nombre_persona)