# ------------------------------------------------------------
# Práctica Control de Flujo 5
#
# Solicita al usuario que indique si sabe programar en Python
# y si tiene conocimientos de inglés.
#
# Las respuestas "sí" y "si" se consideran afirmativas,
# independientemente de si llevan acento o están en mayúsculas.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Solicitar las respuestas al usuario
#
# input() permite al usuario responder las preguntas.
# lower() convierte la respuesta a minúsculas para que "SI",
# "Si", "SI" y otras variantes puedan compararse correctamente.
# ------------------------------------------------------------

sabe_python = input("¿Sabes programar en Python? (Sí/No): ").lower()
habla_ingles = input("¿Sabes inglés? (Sí/No): ").lower()


# ------------------------------------------------------------
# Evaluar las condiciones
#
# Se utiliza in para comprobar si la respuesta corresponde
# a alguna de las formas aceptadas: "sí" o "si".
#
# and comprueba que ambas condiciones se cumplan al mismo tiempo.
# ------------------------------------------------------------

if habla_ingles in ("sí", "si") and sabe_python in ("sí", "si"):
    print("Cumples con los requisitos para postularte")

elif habla_ingles == "no" and sabe_python == "no":
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

elif habla_ingles == "no":
    print("Para postularte, necesitas tener conocimientos de inglés")

else:
    print("Para postularte, necesitas saber programar en Python")