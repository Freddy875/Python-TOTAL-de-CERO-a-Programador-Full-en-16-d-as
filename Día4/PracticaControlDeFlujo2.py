# ------------------------------------------------------------
# Práctica Control de Flujo 2
#
# Verifica si una persona de 16 años sin licencia puede
# conducir.
#
# Una persona puede conducir si tiene 18 años o más y
# cuenta con una licencia.
#
# El programa debe mostrar uno de los siguientes resultados:
#
# - "Puedes conducir"
# - "No puedes conducir aún. Debes tener 18 años y contar con una licencia"
# - "No puedes conducir. Necesitas contar con una licencia"
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir las variables
#
# Se almacena la edad de la persona en la variable edad.
# tiene_licencia almacena un valor booleano que indica si
# la persona cuenta con una licencia.
# ------------------------------------------------------------

edad = 16
tiene_licencia = False


# ------------------------------------------------------------
# Verificar las condiciones
#
# Se utiliza el operador and para comprobar que ambas
# condiciones se cumplan al mismo tiempo:
# la persona debe tener 18 años o más y contar con licencia.
#
# elif permite comprobar si la persona es menor de 18 años.
# Si ninguna de las condiciones anteriores se cumple,
# se ejecuta else, indicando que necesita una licencia.
# ------------------------------------------------------------

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")

elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

else:
    print("No puedes conducir. Necesitas contar con una licencia")