# ------------------------------------------------------------
# Práctica: Funciones con cantidad variable de datos ingresados
# Solicitar números al usuario hasta que ingrese un dato que
# no sea numérico y calcular la suma de todos los números.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Función para sumar los números
# Recibe una lista de números y devuelve la suma de sus valores.
# ------------------------------------------------------------
def sumar_numeros(numeros):
    suma = 0

    for numero in numeros:
        suma += numero

    return suma


# ------------------------------------------------------------
# Solicitar números al usuario
# El ciclo continúa mientras se ingresen valores numéricos.
# Si la conversión falla, se termina el ingreso de datos.
# ------------------------------------------------------------
numeros = []

while True:
    entrada = input("Ingresa un número: ")

    try:
        numero = float(entrada)
        numeros.append(numero)

    except ValueError:
        print("Ingresaste un dato que no es un número. Fin del ingreso.")
        break


# ------------------------------------------------------------
# Llamar a la función y mostrar el resultado
# Se envía la lista completa a la función para sumar sus valores.
# ------------------------------------------------------------
if numeros:
    resultado = sumar_numeros(numeros)
    print(f"La suma de los números ingresados es: {resultado}")
else:
    print("No ingresaste ningún número.")