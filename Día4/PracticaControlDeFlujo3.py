# ------------------------------------------------------------
# Práctica Control de Flujo 3
#
# Para acceder a un determinado puesto de trabajo, el candidato
# debe saber programar en Python y tener conocimientos de inglés.
#
# Se debe evaluar al candidato y mostrar el mensaje correspondiente
# según las condiciones que cumpla.
#
# En este ejercicio se evalúa a un candidato que sabe inglés,
# pero no sabe programar en Python.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir las variables
#
# Se utilizan valores booleanos para indicar si el candidato
# habla inglés y si sabe programar en Python.
# ------------------------------------------------------------

habla_ingles = True
sabe_python = False


# ------------------------------------------------------------
# Evaluar las condiciones
#
# Se utiliza and para comprobar si ambas condiciones son
# verdaderas: hablar inglés y saber programar en Python.
#
# not se utiliza para comprobar cuando una condición es falsa.
#
# elif permite evaluar las diferentes combinaciones posibles
# de las condiciones.
# ------------------------------------------------------------

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")

elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")

else:
    print("Para postularte, necesitas saber programar en Python")