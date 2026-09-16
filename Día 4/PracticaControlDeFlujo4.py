# ------------------------------------------------------------
# Práctica Control de Flujo 4
#
# Solicita al usuario su edad y si cuenta con una licencia.
#
# Después verifica las siguientes condiciones:
#
# - Si tiene 18 años o más y cuenta con licencia, puede conducir.
# - Si es menor de 18 años, no puede conducir aún.
# - Si tiene 18 años o más pero no cuenta con licencia,
#   no puede conducir porque necesita una licencia.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Solicitar los datos al usuario
#
# input() permite al usuario ingresar su edad y responder
# si cuenta con una licencia.
# int() convierte la edad ingresada en un número entero.
# ------------------------------------------------------------

edad = int(input("Ingresa tu edad: "))
tiene_licencia = input("¿Tienes licencia? (Sí/No): ")


# ------------------------------------------------------------
# Verificar las condiciones
#
# Se utiliza and para comprobar que la persona tenga 18 años
# o más y que además cuente con una licencia.
#
# elif comprueba si la persona es menor de 18 años.
#
# Si ninguna de las condiciones anteriores se cumple,
# significa que tiene la edad requerida pero no cuenta
# con una licencia.
# ------------------------------------------------------------

if edad >= 18 and tiene_licencia.lower() == "sí":
    print("Puedes conducir")

elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

else:
    print("No puedes conducir. Necesitas contar con una licencia")