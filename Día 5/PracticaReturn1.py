# ------------------------------------------------------------
# Práctica Return 1
# Crear una función llamada potencia que reciba dos valores
# numéricos como argumentos: una base y un exponente.
# La función debe devolver el resultado de la potencia.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función potencia
# Recibe la base y el exponente como argumentos.
# Calcula la potencia y devuelve el resultado.
# ------------------------------------------------------------

def potencia(base, exponente):
    return base ** exponente


# ------------------------------------------------------------
# Pedir los datos al usuario
# Se solicita la base y el exponente y se convierten
# a números enteros.
# ------------------------------------------------------------

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))


# ------------------------------------------------------------
# Llamar a la función
# Se envían la base y el exponente a la función.
# El resultado que devuelve return se guarda en resultado.
# ------------------------------------------------------------

resultado = potencia(base, exponente)


# ------------------------------------------------------------
# Mostrar el resultado
# Se muestra la potencia calculada al usuario.
# ------------------------------------------------------------

print(f"El resultado de {base} elevado a {exponente} es {resultado}")