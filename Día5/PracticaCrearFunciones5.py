# ------------------------------------------------------------
# Práctica Crear Funciones 5
# Crear una función llamada cuadrado que reciba un número
# como argumento y muestre en pantalla el cuadrado de ese número.
# Pedir el número al usuario y llamar a la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función cuadrado
# Recibe un número mediante el argumento un_numero.
# Calcula el cuadrado del número y muestra el resultado.
# ------------------------------------------------------------

def cuadrado(un_numero):
    print(f"Tu número {un_numero} elevado al cuadrado es {un_numero ** 2}")


# ------------------------------------------------------------
# Pedir un número al usuario
# El número ingresado se convierte a entero y se guarda
# en la variable un_numero.
# ------------------------------------------------------------

un_numero = int(input("Ingresa un número: "))


# ------------------------------------------------------------
# Llamar a la función
# Se envía el número ingresado por el usuario como argumento.
# ------------------------------------------------------------

cuadrado(un_numero)