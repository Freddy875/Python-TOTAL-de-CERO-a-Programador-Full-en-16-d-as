# ------------------------------------------------------------
# Práctica sobre Argumentos Indefinidos (*args) 4
# Solicitar números al usuario hasta que ingrese un dato
# no numérico y calcular la suma de sus valores al cuadrado.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para sumar los cuadrados
# *numeros recibe una cantidad indeterminada de argumentos.
# sum() suma el cuadrado de cada número recibido.
# ------------------------------------------------------------
def suma_cuadrados(*numeros):
    return sum(num ** 2 for num in numeros)


# ------------------------------------------------------------
# Informar al usuario sobre el funcionamiento del programa.
# ------------------------------------------------------------
print("Este programa sumará los cuadrados de los números que ingreses.")
print("Ingresa números uno por uno.")
print("Para terminar e imprimir el resultado, ingresa algo que no sea un número.")


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
resultado = suma_cuadrados(*numeros)

print(f"La suma de los cuadrados es: {resultado}")