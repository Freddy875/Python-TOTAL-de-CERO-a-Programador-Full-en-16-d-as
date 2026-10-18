# ------------------------------------------------------------
# Práctica Operadores Lógicos 3
#
# Verifica si las palabras almacenadas en palabra1 y palabra2
# no se encuentran en la frase indicada.
#
# - palabra1 = "éxito"
# - palabra2 = "tecnología"
#
# El resultado de esta comprobación debe almacenarse en una
# variable llamada mi_bool.
# ------------------------------------------------------------


# Definir la frase y las palabras

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"


# ------------------------------------------------------------
# Verificar las condiciones
# Se utiliza el operador not in para comprobar que cada palabra
# no se encuentre dentro de la frase.
# El operador and permite comprobar ambas condiciones al mismo
# tiempo.
# El resultado se almacena en mi_bool.
# ------------------------------------------------------------

# Verificar si ambas palabras NO están en la frase

mi_bool = palabra1 not in frase and palabra2 not in frase


# ------------------------------------------------------------
# Imprimir el resultado
# Se muestra el valor booleano obtenido de la comprobación.
# True indica que ambas palabras no se encuentran en la frase.
# ------------------------------------------------------------

# Imprimir el resultado

print(mi_bool)  # Esto imprimirá True si ambas palabras no están en la frase