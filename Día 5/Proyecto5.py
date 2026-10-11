from random import choice


# ----------------------------------------
# LISTA DE PALABRAS Y CONFIGURACIÓN
# ----------------------------------------

# Palabras posibles para el juego: combinamos las de nuestra versión
# con las que proporcionó el profesor.
palabras = [
    "python",
    "programacion",
    "funciones",
    "variable",
    "teclado",
    "panadero",
    "dinosaurio",
    "helipuerto",
    "tiburon"
]


# ----------------------------------------
# MOSTRAR EL ESTADO DE LA PALABRA
# ----------------------------------------

def mostrar_palabra(palabra, letras):
    """
    Construye una representación de la palabra secreta.

    Muestra las letras que el jugador ha adivinado y utiliza
    guiones bajos para representar las letras pendientes.

    Parámetros:
        palabra: palabra secreta que debe adivinarse.
        letras: lista de letras que el jugador ha acertado.

    Devuelve:
        Una cadena con las letras descubiertas y los guiones.
    """
    palabra_mostrada = ""

    for letra in palabra:
        if letra in letras:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    return palabra_mostrada.strip()


# ----------------------------------------
# PEDIR Y VALIDAR UNA LETRA
# ----------------------------------------

def pedir_letra():
    """
    Solicita una letra al jugador y valida su entrada.

    Comprueba que la entrada tenga un solo carácter y que
    sea una letra alfabética. Si no es válida, vuelve a pedirla.

    Devuelve:
        La letra introducida en minúsculas y sin espacios
        al principio o al final.
    """
    while True:
        letra = input("Introduce una letra: ").lower().strip()

        if len(letra) != 1 or not letra.isalpha():
            print("Introduce solamente una letra.")
        else:
            return letra


# ----------------------------------------
# COMPROBAR SI EL JUGADOR HA GANADO
# ----------------------------------------

def ha_ganado(palabra, letras):
    """
    Comprueba si el jugador ha descubierto todas las letras
    de la palabra secreta.

    Parámetros:
        palabra: palabra que debe adivinarse.
        letras: letras que el jugador ha acertado.

    Devuelve:
        True si todas las letras están descubiertas.
        False si todavía falta alguna letra.
    """
    for letra in palabra:
        if letra not in letras:
            return False

    return True


# ----------------------------------------
# DESARROLLO Y CONTROL DEL JUEGO
# ----------------------------------------

def jugar():
    """
    Coordina el desarrollo completo de una partida.

    Selecciona la palabra secreta, inicializa las letras
    adivinadas y las vidas, y controla los turnos hasta que
    el jugador adivine la palabra o se quede sin vidas.
    """

    # Selecciona aleatoriamente la palabra secreta.
    palabra_secreta = choice(palabras)

    # Guarda las letras acertadas durante la partida.
    letras_adivinadas = []

    # Establece las seis vidas iniciales del jugador.
    vidas = 6

    print("¡Bienvenido al juego del Ahorcado!")

    # Continúa mientras queden vidas y el jugador no haya ganado.
    while vidas > 0 and not ha_ganado(
        palabra_secreta, letras_adivinadas
    ):

        # Muestra las letras descubiertas y las vidas disponibles.
        print(
            "\nPalabra:",
            mostrar_palabra(palabra_secreta, letras_adivinadas)
        )
        print("Vidas restantes:", vidas)

        # Solicita una letra al jugador.
        letra = pedir_letra()

        # Evita que una letra repetida consuma una vida.
        if letra in letras_adivinadas:
            print("Ya habías probado esa letra. Intenta con otra.")
            continue

        # Registra la letra introducida.
        letras_adivinadas.append(letra)

        # Si la letra no aparece en la palabra, resta una vida.
        if letra in palabra_secreta:
            print("¡Correcto! La letra está en la palabra.")
        else:
            vidas -= 1
            print("La letra no está en la palabra. Pierdes una vida.")

    # ----------------------------------------
    # RESULTADO FINAL
    # ----------------------------------------

    # Informa al jugador si descubrió la palabra o perdió.
    if ha_ganado(palabra_secreta, letras_adivinadas):
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print("\nTe has quedado sin vidas.")
        print("La palabra secreta era:", palabra_secreta)


# ----------------------------------------
# INICIAR EL JUEGO
# ----------------------------------------

# Llama a la función principal para comenzar la partida.
jugar()