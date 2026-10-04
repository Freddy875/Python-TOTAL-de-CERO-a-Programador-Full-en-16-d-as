# ------------------------------------------------------------
# Práctica Funciones Dinámicas 2
# Crear una función llamada suma_menores que reciba una lista
# de números y sume únicamente los valores mayores a 0
# y menores a 1000.
# La función debe devolver el resultado de la suma.
# La lista debe almacenarse en la variable lista_numeros.
# No se debe invocar la función.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función suma_menores
# Recibe una lista de números como argumento.
# Suma únicamente los números que sean mayores a 0
# y menores a 1000.
# ------------------------------------------------------------

def suma_menores(lista):
    return sum(num for num in lista if 0 < num < 1000)  # Suma solo los valores dentro del rango


# ------------------------------------------------------------
# Crear la lista de números
# La lista contiene valores dentro y fuera del rango permitido.
# ------------------------------------------------------------

lista_numeros = [10, 500, 1200, -5, 750, 999, 1500, 0]


# ------------------------------------------------------------
# No se invoca la función
# La práctica únicamente solicita definir la función
# y crear la lista.
# ------------------------------------------------------------