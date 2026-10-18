# ------------------------------------------------------------
# Práctica Loop For 1
#
# Utilizando loops For, saluda a todos los miembros de una
# clase, imprimiendo "Hola" seguido de su nombre.
#
# Por ejemplo:
# "Hola María"
# ------------------------------------------------------------


# ------------------------------------------------------------
# Crear la lista de alumnos
#
# Se almacenan los nombres de todos los alumnos de la clase
# dentro de una lista.
# ------------------------------------------------------------

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]


# ------------------------------------------------------------
# Recorrer la lista y saludar a cada alumno
#
# for recorre cada elemento de la lista alumnos_clase.
# En cada vuelta, la variable alumno almacena temporalmente
# el nombre del alumno que se está recorriendo.
#
# f-string permite insertar el nombre del alumno dentro
# del mensaje.
# ------------------------------------------------------------

for alumno in alumnos_clase:
    print(f"Hola {alumno}")