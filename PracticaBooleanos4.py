# ------------------------------------------------------------
# Práctica Booleanos 2
# Verifica la relación entre los resultados de 17834 / 34
# y 87 * 56, mostrando primero cada operación.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Primera operación
# Se divide 17834 entre 34 y se muestra el resultado.
# ------------------------------------------------------------

operacion_1 = 17834 / 34

print(f"El resultado de 17834 / 34 es: {operacion_1}")


# ------------------------------------------------------------
# Segunda operación
# Se multiplica 87 por 56 y se muestra el resultado.
# ------------------------------------------------------------

operacion_2 = 87 * 56

print(f"El resultado de 87 * 56 es: {operacion_2}")


# ------------------------------------------------------------
# Comparar los resultados
# Se utilizan operadores de comparación para identificar la
# relación entre el resultado de ambas operaciones.
# ------------------------------------------------------------

if operacion_1 > operacion_2:
    print("La primera operación es mayor que la segunda.")

elif operacion_1 < operacion_2:
    print("La primera operación es menor que la segunda.")

elif operacion_1 == operacion_2:
    print("Ambas operaciones son iguales.")

elif operacion_1 >= operacion_2:
    print("La primera operación es mayor o igual que la segunda.")

elif operacion_1 <= operacion_2:
    print("La primera operación es menor o igual que la segunda.")

elif operacion_1 != operacion_2:
    print("Los resultados son diferentes.")