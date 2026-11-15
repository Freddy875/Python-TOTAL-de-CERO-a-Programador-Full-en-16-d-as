# ------------------------------------------------------------
# Práctica Funciones Dinamicas 5
# Pedir dos números al usuario y validar si su suma tiene
# 3 cifras utilizando range().
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función validar_suma
# Recibe dos números, calcula su suma y verifica si está
# entre 100 y 999.
# ------------------------------------------------------------

def validar_suma(numero1, numero2):
    suma = numero1 + numero2
    return suma in range(100, 1000)


# ------------------------------------------------------------
# Pedir los dos números al usuario
# Los valores ingresados se convierten a enteros.
# ------------------------------------------------------------

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))


# ------------------------------------------------------------
# Calcular la suma
# Se suman los dos números ingresados por el usuario.
# ------------------------------------------------------------

suma = numero1 + numero2


# ------------------------------------------------------------
# Llamar a la función
# Se envían los dos números como argumentos.
# ------------------------------------------------------------

resultado = validar_suma(numero1, numero2)


# ------------------------------------------------------------
# Mostrar los números y el resultado
# Se muestran los dos números ingresados, su suma y
# se indica si la suma tiene 3 cifras.
# ------------------------------------------------------------

print(f"\nPrimer número: {numero1}")
print(f"Segundo número: {numero2}")
print(f"Suma: {suma}")

if resultado:
    print("La suma tiene 3 cifras.")
else:
    print("La suma no tiene 3 cifras.")