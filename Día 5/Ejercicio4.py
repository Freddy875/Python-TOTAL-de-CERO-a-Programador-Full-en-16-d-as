# ------------------------------------------------------------
# Ejercicio 4
# Crear una función que muestre los números primos desde 0
# hasta el número recibido, incluido, y devuelva su cantidad.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para comprobar y contar los números primos.
# Un número primo solo es divisible entre 1 y él mismo.
# La función muestra los primos encontrados y devuelve
# la cantidad total.
# ------------------------------------------------------------
def contar_primos(numero):
    cantidad_primos = 0

    for numero_actual in range(2, numero + 1):
        es_primo = True

        for divisor in range(2, numero_actual):
            if numero_actual % divisor == 0:
                es_primo = False
                break

        if es_primo:
            print(numero_actual)
            cantidad_primos += 1

    return cantidad_primos


# ------------------------------------------------------------
# Solicitar al usuario el límite superior del rango.
# ------------------------------------------------------------
numero = int(input("Ingresa un número entero positivo: "))


# ------------------------------------------------------------
# Llamar a la función y mostrar la cantidad de primos.
# ------------------------------------------------------------
cantidad = contar_primos(numero)

print(f"Se encontraron {cantidad} números primos.")