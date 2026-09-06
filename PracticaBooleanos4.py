# ------------------------------------------------------------
# Práctica Booleanos 4
# Verifica si 17834 / 34 es mayor que 87 * 56 y muestra
# los resultados de las operaciones antes de realizar la
# comparación.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Primera operación
# Se divide 17834 entre 34 y se guarda el resultado.
# ------------------------------------------------------------

operacion_1 = 17834 / 34

print(f"El resultado de 17834 / 34 es: {operacion_1}")
# Imprime: El resultado de 17834 / 34 es: 524.5294117647059


# ------------------------------------------------------------
# Segunda operación
# Se multiplica 87 por 56 y se guarda el resultado.
# ------------------------------------------------------------

operacion_2 = 87 * 56

print(f"El resultado de 87 * 56 es: {operacion_2}")
# Imprime: El resultado de 87 * 56 es: 4872


# ------------------------------------------------------------
# Comparación mayor que
# El operador > comprueba si el resultado de la primera
# operación es mayor que el resultado de la segunda.
# ------------------------------------------------------------

print(f"¿{operacion_1} es mayor que {operacion_2}? {operacion_1 > operacion_2}")
# Imprime: ¿524.5294117647059 es mayor que 4872? False


# ------------------------------------------------------------
# Comparar los resultados mediante condicionales
# Se comprueba si el primer resultado es mayor, menor o igual
# que el segundo resultado.
# ------------------------------------------------------------

if operacion_1 > operacion_2:
    print("La primera operación es mayor que la segunda.")

elif operacion_1 < operacion_2:
    print("La primera operación es menor que la segunda.")

else:
    print("Ambas operaciones son iguales.")