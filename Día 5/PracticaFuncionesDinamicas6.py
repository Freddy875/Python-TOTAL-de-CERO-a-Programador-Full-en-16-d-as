# ------------------------------------------------------------
# Práctica Funciones Dinámicas 6
# Pedir al usuario 5 números y utilizar una función para
# contar cuántos son positivos y cuántos son negativos.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función contar_positivos_negativos
# Recibe una lista de números.
# Cuenta por separado los números positivos y negativos.
# Finalmente devuelve ambas cantidades.
# ------------------------------------------------------------

def contar_positivos_negativos(lista):
    positivos = sum(1 for num in lista if num > 0)
    negativos = sum(1 for num in lista if num < 0)

    return positivos, negativos


# ------------------------------------------------------------
# Pedir 5 números al usuario
# Los números ingresados se almacenan en una lista.
# ------------------------------------------------------------

lista_numeros = []

for i in range(5):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    lista_numeros.append(numero)


# ------------------------------------------------------------
# Llamar a la función
# Se envía la lista como argumento.
# La función devuelve la cantidad de positivos y negativos.
# ------------------------------------------------------------

positivos, negativos = contar_positivos_negativos(lista_numeros)


# ------------------------------------------------------------
# Mostrar el resultado
# Se muestran las cantidades que devolvió la función.
# ------------------------------------------------------------

print(f"Tienes {positivos} números positivos y {negativos} números negativos.")