# ------------------------------------------------------------
# Práctica Funciones Dinamicas 4
# Crear una función que reciba un número y valide si tiene
# exactamente 3 cifras.
# Pedir el número al usuario y mostrar el resultado.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función validar_tres_cifras
# Recibe un número como argumento.
# Verifica si el número está entre 100 y 999.
# return devuelve True si tiene 3 cifras y False si no.
# ------------------------------------------------------------

def validar_tres_cifras(numero):
    return 100 <= numero <= 999


# ------------------------------------------------------------
# Pedir un número al usuario
# El valor ingresado se convierte a entero.
# ------------------------------------------------------------

numero = int(input("Ingresa un número: "))


# ------------------------------------------------------------
# Llamar a la función
# Se envía el número ingresado como argumento.
# El resultado que devuelve return se guarda en resultado.
# ------------------------------------------------------------

resultado = validar_tres_cifras(numero)


# ------------------------------------------------------------
# Mostrar el resultado
# Se informa al usuario si el número tiene 3 cifras.
# ------------------------------------------------------------

if resultado:
    print("El número tiene 3 cifras.")
else:
    print("El número no tiene 3 cifras.")