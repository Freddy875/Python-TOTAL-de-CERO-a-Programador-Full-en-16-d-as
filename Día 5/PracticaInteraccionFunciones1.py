# ------------------------------------------------------------
# Práctica sobre Interacción entre Funciones 1
# Crear una función llamada lanzar_dados que genere dos
# valores aleatorios entre 1 y 6 y devuelva ambos resultados.
# Crear otra función llamada evaluar_jugada que reciba los
# resultados, calcule su suma y devuelva un mensaje según
# las condiciones indicadas.
# No se deben invocar las funciones.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Importar la biblioteca random
# Permite generar números aleatorios para simular los dados.
# ------------------------------------------------------------

import random  # Importar la librería para generar números aleatorios


# ------------------------------------------------------------
# Definir la función lanzar_dados
# No recibe argumentos.
# Genera dos números aleatorios entre 1 y 6, simulando
# el lanzamiento de dos dados.
# return devuelve ambos valores.
# ------------------------------------------------------------

def lanzar_dados():
    dado1 = random.randint(1, 6)  # Generar un número entre 1 y 6
    dado2 = random.randint(1, 6)  # Generar otro número entre 1 y 6
    return dado1, dado2  # Retorna los dos valores de los dados


# ------------------------------------------------------------
# Definir la función evaluar_jugada
# Recibe los resultados de los dos dados como argumentos.
# Calcula la suma y devuelve un mensaje según el resultado.
# ------------------------------------------------------------

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2  # Calcular la suma de los dos dados

    # --------------------------------------------------------
    # Evaluar el resultado según las condiciones dadas
    # Si la suma es menor o igual a 6, devuelve "Lamentable".
    # Si la suma es mayor a 6 y menor a 10, indica que hay
    # buenas chances.
    # Si la suma es mayor o igual a 10, indica una jugada
    # ganadora.
    # --------------------------------------------------------

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# ------------------------------------------------------------
# No invocar las funciones
# La práctica solicita definir ambas funciones, pero no
# ejecutarlas todavía.
# ------------------------------------------------------------