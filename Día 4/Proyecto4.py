# ------------------------------------------------------------
# Proyecto del Día 4
# Juego de adivinar un número.
# El programa genera un número secreto entre 1 y 100
# y el usuario tiene 8 intentos para adivinarlo.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Importamos la librería random para generar
# el número secreto de manera aleatoria.
# ------------------------------------------------------------

import random


# ------------------------------------------------------------
# Pedimos el nombre del usuario para poder utilizarlo
# durante el juego.
# ------------------------------------------------------------

nombre = input("¿Cuál es tu nombre? ")


# ------------------------------------------------------------
# Generamos un número aleatorio entre 1 y 100.
# Este será el número que el usuario deberá adivinar.
# ------------------------------------------------------------

numero_secreto = random.randint(1, 101)


# ------------------------------------------------------------
# Informamos al usuario que el juego comienza
# y que tiene 8 intentos para adivinar el número.
# ------------------------------------------------------------

print(
    f"Hola, {nombre}, he pensado un número entre 1 y 100 "
    "y tienes solo 8 intentos para adivinarlo."
)


# ------------------------------------------------------------
# El loop permite realizar hasta 8 intentos.
# La variable intento indica el número de intento actual.
# ------------------------------------------------------------

for intento in range(1, 9):

    # --------------------------------------------------------
    # Pedimos al usuario que introduzca un número.
    # --------------------------------------------------------

    numero = int(input(f"\nIntento {intento}: Elige un número: "))


    # --------------------------------------------------------
    # Verifica que el número elegido esté dentro del rango
    # permitido: desde 1 hasta 100.
    # --------------------------------------------------------

    if numero < 1 or numero > 100:
        print("Has elegido un número que no está permitido.")


    # --------------------------------------------------------
    # Verifica si el número elegido es menor
    # que el número secreto.
    # --------------------------------------------------------

    elif numero < numero_secreto:
        print(
            "Respuesta incorrecta. "
            "Has elegido un número menor al número secreto."
        )


    # --------------------------------------------------------
    # Verifica si el número elegido es mayor
    # que el número secreto.
    # --------------------------------------------------------

    elif numero > numero_secreto:
        print(
            "Respuesta incorrecta. "
            "Has elegido un número mayor al número secreto."
        )


    # --------------------------------------------------------
    # Si ninguna de las condiciones anteriores se cumple,
    # significa que el usuario acertó el número secreto.
    # --------------------------------------------------------

    else:
        print(
            f"¡Has ganado, {nombre}! "
            f"Has acertado en {intento} intentos."
        )
        break


# ------------------------------------------------------------
# Si el loop termina sin utilizar break, significa que se
# agotaron los 8 intentos sin acertar el número.
# ------------------------------------------------------------

else:
    print(
        f"\nSe han agotado tus 8 intentos. "
        f"El número secreto era {numero_secreto}."
    )
