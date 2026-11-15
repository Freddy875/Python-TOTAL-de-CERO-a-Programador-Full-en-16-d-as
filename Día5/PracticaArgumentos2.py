# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (*args) 2
# Solicitar números al usuario hasta que ingrese un dato
# no numérico y sumar los valores absolutos ingresados.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para sumar los valores absolutos
# *numeros recibe una cantidad variable de argumentos.
# abs() obtiene el valor absoluto de cada número.
# sum() suma todos los valores absolutos.
# ------------------------------------------------------------
def suma_absolutos(*numeros):
    return sum(abs(numero) for numero in numeros)


# ------------------------------------------------------------
# Explicar al usuario cómo funciona el programa.
# ------------------------------------------------------------
print("Este programa sumará los valores absolutos de los números.")
print("Ingresa números uno por uno.")
print("Para terminar y obtener el resultado, ingresa algo que no sea un número.")


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
# Llamar a la función y mostrar el resultado.
# *numeros desempaqueta la lista en argumentos individuales.
# ------------------------------------------------------------
resultado = suma_absolutos(*numeros)

print(f"La suma de los valores absolutos es: {resultado}")