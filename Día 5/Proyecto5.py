from random import choice

# ----------------------------------------
# LISTA DE PALABRAS Y CONFIGURACIÓN
# ----------------------------------------

palabras = ["python", "programacion", "funciones", "variable", "teclado", "panadero", "dinosaurio", "helipuerto", "tiburon"]

palabra_secreta = choice(palabras)
letras_adivinadas = []
vidas = 6


# ----------------------------------------
# MOSTRAR EL ESTADO DE LA PALABRA
# ----------------------------------------

def mostrar_palabra(palabra, letras):
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
    for letra in palabra:
        if letra not in letras:
            return False

    return True


# ----------------------------------------
# DESARROLLO DEL JUEGO
# ----------------------------------------

print("¡Bienvenido al juego del Ahorcado!")

while vidas > 0 and not ha_ganado(palabra_secreta, letras_adivinadas):

    print("\nPalabra:", mostrar_palabra(palabra_secreta, letras_adivinadas))
    print("Vidas restantes:", vidas)

    letra = pedir_letra()

    if letra in letras_adivinadas:
        print("Ya habías probado esa letra. Intenta con otra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra_secreta:
        print("¡Correcto! La letra está en la palabra.")
    else:
        vidas -= 1
        print("La letra no está en la palabra. Pierdes una vida.")


# ----------------------------------------
# RESULTADO FINAL
# ----------------------------------------

if ha_ganado(palabra_secreta, letras_adivinadas):
    print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
else:
    print("\nTe has quedado sin vidas.")
    print("La palabra secreta era:", palabra_secreta)