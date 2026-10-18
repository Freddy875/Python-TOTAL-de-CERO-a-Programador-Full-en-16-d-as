# ------------------------------------------------------------
# Función para sumar una cantidad variable de números.
# *args permite recibir los números como argumentos individuales.
# ------------------------------------------------------------
def sumar_numeros(*args):
    return sum(args)


# ------------------------------------------------------------
# Solicitar números hasta que se ingrese un dato no numérico.
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
# Llamar a la función y mostrar la suma total.
# El operador * desempaqueta la lista en argumentos individuales.
# ------------------------------------------------------------
resultado = sumar_numeros(*numeros)
print(f"La suma de los números ingresados es: {resultado}")