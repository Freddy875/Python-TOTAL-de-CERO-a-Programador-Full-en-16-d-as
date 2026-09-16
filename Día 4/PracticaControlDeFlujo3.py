# ------------------------------------------------------------
# Práctica Control de Flujo 5
#
# Solicita al usuario que indique si sabe programar en Python
# y si tiene conocimientos de inglés.
#
# Después se evalúan las respuestas para determinar si cumple
# con los requisitos para postularse.
# ------------------------------------------------------------

 
# ------------------------------------------------------------
# Solicitar las respuestas al usuario
#
# input() permite al usuario indicar si sabe programar en Python
# y si tiene conocimientos de inglés.
#
# lower() convierte la respuesta a minúsculas para facilitar
# la comparación con "sí" o "no".
# ------------------------------------------------------------

sabe_python = input("¿Sabes programar en Python? (Sí/No): ").lower()
habla_ingles = input("¿Sabes inglés? (Sí/No): ").lower()


# ------------------------------------------------------------
# Evaluar las condiciones
#
# Se utiliza and para comprobar que el usuario cumpla con
# ambos requisitos: saber programar en Python y saber inglés.
#
# elif permite comprobar las diferentes combinaciones posibles.
#
# not no es necesario en esta versión, ya que las respuestas
# se comparan directamente con "sí" o "no".
# ------------------------------------------------------------

if habla_ingles == "si" and sabe_python == "si":
    print("Cumples con los requisitos para postularte")

elif habla_ingles == "no" and sabe_python == "no":
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

elif habla_ingles == "no":
    print("Para postularte, necesitas tener conocimientos de inglés")

else:
    print("Para postularte, necesitas saber programar en Python")