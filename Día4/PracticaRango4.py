# ------------------------------------------------------------
# Práctica Rango 3
# Calcula la suma de los cuadrados de los números del 1 al 15.
# Muestra cada número, su cuadrado y cómo se va acumulando la suma.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Variable para almacenar la suma acumulada.
# Comienza en 0 porque todavía no se ha sumado ningún cuadrado.
# ------------------------------------------------------------

suma_cuadrados = 0

# ------------------------------------------------------------
# Recorre los números del 1 al 15.
# En cada vuelta se calcula el cuadrado del número.
# ------------------------------------------------------------

for numero in range(1, 16):

    # Calcula el cuadrado del número actual.
    cuadrado = numero ** 2

    # Suma el cuadrado a la suma acumulada.
    suma_cuadrados += cuadrado

    # Muestra el número, su cuadrado y la operación de la suma.
    print(
        f"{numero} al cuadrado = {cuadrado} | "
        f"Suma acumulada: {suma_cuadrados - cuadrado} + {cuadrado} = {suma_cuadrados}"
    )

# ------------------------------------------------------------
# Muestra el resultado final de la suma de todos los cuadrados.
# ------------------------------------------------------------

print(f"\nResultado final: {suma_cuadrados}")