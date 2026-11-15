# ------------------------------------------------------------
# Práctica Funciones Dinámicas 7
# Pedir números al usuario hasta que indique que no quiere
# agregar otro.
# Después, utilizar una función para contar cuántos números
# son pares y cuántos son impares.
# El número 0 no se contará como par ni como impar.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función cantidad_pares_impares
# Recibe una lista de números.
# Cuenta por separado los números pares e impares.
# El 0 no se cuenta en ninguna de las dos categorías.
# ------------------------------------------------------------

def cantidad_pares_impares(lista):
    pares = sum(1 for num in lista if num != 0 and num % 2 == 0)
    impares = sum(1 for num in lista if num != 0 and num % 2 != 0)

    return pares, impares


# ------------------------------------------------------------
# Crear una lista vacía
# En esta lista se almacenarán los números ingresados.
# ------------------------------------------------------------

lista_numeros = []


# ------------------------------------------------------------
# Pedir números al usuario
# El ciclo continúa hasta que el usuario responda "no".
# ------------------------------------------------------------

while True:
    numero = int(input("Ingresa un número: "))
    lista_numeros.append(numero)

    continuar = input("¿Quieres agregar otro? (Sí/No): ").lower()

    if continuar == "no":
        break


# ------------------------------------------------------------
# Llamar a la función
# Se envía la lista de números como argumento.
# La función devuelve la cantidad de pares y de impares.
# ------------------------------------------------------------

pares, impares = cantidad_pares_impares(lista_numeros)


# ------------------------------------------------------------
# Mostrar el resultado
# Se muestran las cantidades de números pares e impares.
# ------------------------------------------------------------

print(f"Tienes {pares} números pares y {impares} números impares.")