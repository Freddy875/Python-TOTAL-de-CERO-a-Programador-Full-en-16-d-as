# ------------------------------------------------------------
# Práctica Funciones Dinámicas 3
# Crear una función llamada cantidad_pares que reciba una
# lista de números y cuente cuántos números pares contiene.
# La función debe devolver el resultado de dicha cuenta.
# La lista debe almacenarse en la variable lista_numeros.
# No se debe invocar la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función cantidad_pares
# Recibe una lista de números como argumento.
# Cuenta los números pares utilizando el operador %.
# Si el residuo de dividir un número entre 2 es 0,
# significa que el número es par.
# ------------------------------------------------------------

def cantidad_pares(lista):
    return sum(1 for num in lista if num % 2 == 0)  # Suma 1 por cada número par encontrado


# ------------------------------------------------------------
# Crear la lista de números
# La lista contiene números pares e impares.
# ------------------------------------------------------------

lista_numeros = [10, 5, 8, 3, 7, 12, 14, 21, 30]


# ------------------------------------------------------------
# No se invoca la función
# La práctica únicamente solicita definir la función
# y crear la lista.
# ------------------------------------------------------------