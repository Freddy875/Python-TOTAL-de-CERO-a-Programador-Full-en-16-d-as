# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (*args) 3
# Solicitar el nombre y una cantidad indeterminada de números.
# Finalizar cuando el usuario ingrese un dato no numérico
# y mostrar la suma de los números ingresados.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para sumar los números de una persona
# nombre recibe el nombre como primer argumento.
# *numeros recibe una cantidad variable de números.
# sum() calcula la suma de todos los números recibidos.
# La función devuelve un mensaje con el nombre y la suma.
# ------------------------------------------------------------
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


# ------------------------------------------------------------
# Solicitar el nombre del usuario.
# ------------------------------------------------------------
nombre = input("Ingresa tu nombre: ")


# ------------------------------------------------------------
# Informar cómo funciona el ingreso de números.
# ------------------------------------------------------------
print("Ingresa los números que deseas sumar.")
print("Para terminar, escribe algo que no sea un número.")


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
resultado = numeros_persona(nombre, *numeros)

print(resultado)