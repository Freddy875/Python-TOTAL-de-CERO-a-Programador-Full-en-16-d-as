# ------------------------------------------------------------
# Funciones 4
# Solicitar números continuamente hasta que el usuario ingrese
# un dato que no sea numérico. Después, eliminar duplicados
# y calcular el promedio de los números únicos.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Elimina los números duplicados de la lista.
# ------------------------------------------------------------
def reducir_lista(lista):
    lista_unica = list(set(lista))
    return lista_unica


# ------------------------------------------------------------
# Calcula el promedio de los números de la lista.
# ------------------------------------------------------------
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0


# ------------------------------------------------------------
# Solicita números hasta que el usuario ingrese un dato
# que no sea numérico.
# ------------------------------------------------------------
print("Ingresa números uno por uno.")
print("El programa continuará preguntando hasta que ingreses algo que no sea un número.")

lista_numeros = []

while True:
    entrada = input("Ingresa un número: ")

    try:
        numero = float(entrada)
        lista_numeros.append(numero)
    except ValueError:
        print("Ingresaste un dato que no es un número. Fin del ingreso.")
        break


# ------------------------------------------------------------
# Llama a las funciones y muestra los resultados.
# ------------------------------------------------------------
if lista_numeros:
    lista_reducida = reducir_lista(lista_numeros)
    print(f"Lista sin duplicados: {lista_reducida}")

    resultado_promedio = promedio(lista_reducida)
    print(f"Promedio: {resultado_promedio:.2f}")
else:
    print("No ingresaste ningún número.")