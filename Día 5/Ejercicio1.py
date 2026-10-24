# ------------------------------------------------------------
# Ejercicio 1
# Crear una función que reciba tres números enteros.
# Si su suma es mayor a 15, devuelve el mayor.
# Si su suma es menor a 10, devuelve el menor.
# Si su suma está entre 10 y 15, ambos incluidos,
# devuelve el número intermedio.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Función para devolver un número según la suma.
# max() obtiene el número mayor.
# min() obtiene el número menor.
# sorted() ordena los números de menor a mayor.
# ------------------------------------------------------------
def devolver_distintos(numero1, numero2, numero3):
    suma_numeros = numero1 + numero2 + numero3
    lista_numeros = [numero1, numero2, numero3] ### Un pequeño cambio para optimizar el codigo

    if suma_numeros > 15:
        return max(lista_numeros)

    elif suma_numeros < 10:
        return min(lista_numeros)

    else:
        numeros_ordenados = sorted(lista_numeros)
        return numeros_ordenados[1]


# ------------------------------------------------------------
# Solicitar los tres números al usuario.
# int() convierte las entradas en números enteros.
# ------------------------------------------------------------
numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))
numero3 = int(input("Ingresa el tercer número entero: "))


# ------------------------------------------------------------
# Llamar a la función y mostrar el resultado.
# ------------------------------------------------------------
resultado = devolver_distintos(numero1, numero2, numero3)

print(f"El número seleccionado es: {resultado}")