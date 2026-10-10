# ------------------------------------------------------------
# Práctica sobre Interacción entre Funciones 4
# Simular el lanzamiento de dos dados y evaluar el resultado.
# Se llamarán las funciones lanzar_dados() y evaluar_jugada()
# para mostrar al usuario el resultado de su jugada.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Importar la biblioteca random
# Permite generar números aleatorios para los dados.
# ------------------------------------------------------------

import random


# ------------------------------------------------------------
# Definir la función lanzar_dados
# Genera dos números aleatorios entre 1 y 6.
# Devuelve los resultados de ambos dados.
# ------------------------------------------------------------

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2


# ------------------------------------------------------------
# Definir la función evaluar_jugada
# Recibe los resultados de los dos dados, calcula su suma
# y devuelve un mensaje según el resultado obtenido.
# ------------------------------------------------------------

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# ------------------------------------------------------------
# Explicar el juego al usuario
# Se informa que lanzará dos dados y conocerá el resultado.
# ------------------------------------------------------------

print("¡Vamos a jugar a los dados!")
print("Lanzarás dos dados y evaluaremos el resultado obtenido.")
input("Presiona Enter para lanzar los dados...")


# ------------------------------------------------------------
# Llamar a la función lanzar_dados
# Se obtienen los resultados de los dos dados y se guardan
# en las variables dado1 y dado2.
# ------------------------------------------------------------

dado1, dado2 = lanzar_dados()


# ------------------------------------------------------------
# Mostrar los resultados de los dados
# Se imprime el valor obtenido en cada dado.
# ------------------------------------------------------------

print(f"\nPrimer dado: {dado1}")
print(f"Segundo dado: {dado2}")


# ------------------------------------------------------------
# Llamar a la función evaluar_jugada
# Se envían los resultados de ambos dados como argumentos.
# El mensaje devuelto por return se guarda en resultado.
# ------------------------------------------------------------

resultado = evaluar_jugada(dado1, dado2)


# ------------------------------------------------------------
# Mostrar el resultado final
# Se imprime el mensaje que devuelve la función.
# ------------------------------------------------------------

print(resultado)