# ------------------------------------------------------------
# Ejercicio 3
# Crear una función que reciba una cantidad indefinida de
# números y devuelva True si encuentra dos ceros consecutivos.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para comprobar si hay ceros consecutivos.
# *numeros permite recibir una cantidad indeterminada de números.
# El ciclo recorre cada número y compara el actual con el siguiente.
# ------------------------------------------------------------
def ceros_consecutivos(*numeros):
    for indice in range(len(numeros) - 1):
        if numeros[indice] == 0 and numeros[indice + 1] == 0:
            return True

    return False


# ------------------------------------------------------------
# Solicitar números hasta que el usuario ingrese un dato
# que no sea numérico.
# ------------------------------------------------------------
numeros = []

print("Ingresa números para comprobar si hay dos ceros consecutivos.")
print("Para terminar, escribe algo que no sea un número.")

while True:
    entrada = input("Ingresa un número: ")

    try:
        numero = int(entrada)
        numeros.append(numero)

    except ValueError:
        print("Fin del ingreso de números.")
        break


# ------------------------------------------------------------
# Llamar a la función y mostrar el resultado.
# *numeros desempaqueta la lista como argumentos individuales.
# ------------------------------------------------------------
resultado = ceros_consecutivos(*numeros)

print(f"¿Hay dos ceros consecutivos? {resultado}")