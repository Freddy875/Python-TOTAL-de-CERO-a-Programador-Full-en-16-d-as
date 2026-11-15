from random import shuffle

# lista inicial
palitos = ['-', '--', '---', '----',]

# Mezclar la lista de palitos
def mezclar_palitos(palitos):
    shuffle(palitos)
    return palitos

# Elegir un palito
def elegir_palito(palitos):
    palito_elegido = input("Elige un palito (1-4): ")
    while palito_elegido not in ['1', '2', '3', '4']:
        palito_elegido = input("Entrada inválida. Elige un palito (1-4): ")
    return int(palito_elegido) - 1  # Convertir a índice de lista

# Comprobar el intento del usuario
def comprobar_intento(palitos, indice_elegido):
    if palitos[indice_elegido] == '----':
        print("¡Felicidades! Has encontrado el palito más largo.")
    else:
        print("Lo siento, ese no es el palito más largo. Intenta de nuevo.")

palitos_mezclados = mezclar_palitos(palitos)
indice_elegido = elegir_palito(palitos_mezclados)
comprobar_intento(palitos_mezclados, indice_elegido)
