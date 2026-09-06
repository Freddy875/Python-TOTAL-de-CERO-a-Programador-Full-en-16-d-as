# ------------------------------------------------------------
# Primera operación
# Se divide 17834 entre 34 y se guarda el resultado.
# ------------------------------------------------------------

operacion_1 = 17834 / 34

print(f"El resultado de la operación 1 es: {operacion_1}")


# ------------------------------------------------------------
# Segunda operación
# Se multiplica 87 por 56 y se guarda el resultado.
# ------------------------------------------------------------

operacion_2 = 87 * 56

print(f"El resultado de la operación 2 es: {operacion_2}")


# ------------------------------------------------------------
# Comparar los resultados
# Se comparan los valores numéricos para indicar cuál es
# mayor, cuál es menor o si ambos son iguales.
# En el mensaje final, el resultado de la operación 1 se
# muestra con únicamente 2 decimales.
# ------------------------------------------------------------

if operacion_1 > operacion_2:
    print(f"{operacion_1:.2f} es mayor que {operacion_2}")

elif operacion_1 < operacion_2:
    print(f"{operacion_1:.2f} es menor que {operacion_2}")

else:
    print(f"{operacion_1:.2f} es igual a {operacion_2}")