# ------------------------------------------------------------
# Práctica sobre Interacción entre Funciones 6
# Pedir al usuario que elija Cara o Cruz, lanzar una moneda
# al azar y mostrar si ganó o perdió el volado.
# ------------------------------------------------------------

import random  # Importa la biblioteca para generar resultados aleatorios


# ------------------------------------------------------------
# Función para lanzar la moneda
# No recibe argumentos y devuelve aleatoriamente "Cara" o "Cruz".
# ------------------------------------------------------------
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])


# ------------------------------------------------------------
# Función para comprobar si el usuario ganó el volado
# Recibe la elección del usuario y el resultado de la moneda.
# Compara ambos valores y devuelve un mensaje según el resultado.
# ------------------------------------------------------------
def probar_suerte(eleccion_usuario, resultado_moneda):
    if eleccion_usuario == resultado_moneda:
        return "¡Ganaste el volado!"  # Devuelve el mensaje si acertó
    else:
        return "Perdiste el volado."  # Devuelve el mensaje si falló


# ------------------------------------------------------------
# Solicitar la elección del usuario
# capitalize() convierte la primera letra en mayúscula para
# comparar la respuesta con "Cara" o "Cruz".
# ------------------------------------------------------------
eleccion_usuario = input("Elige Cara o Cruz: ").capitalize()


# ------------------------------------------------------------
# Validar la elección
# Mientras la respuesta no sea "Cara" ni "Cruz", vuelve a pedirla.
# ------------------------------------------------------------
while eleccion_usuario not in ["Cara", "Cruz"]:
    eleccion_usuario = input(
        "Opción inválida. Escribe Cara o Cruz: "
    ).capitalize()


# ------------------------------------------------------------
# Ejecutar las funciones y mostrar el resultado
# Primero se lanza la moneda, después se muestra el resultado
# aleatorio y finalmente se indica si el usuario ganó o perdió.
# ------------------------------------------------------------
resultado_moneda = lanzar_moneda()

print(f"La moneda cayó en: {resultado_moneda}")
print(probar_suerte(eleccion_usuario, resultado_moneda))