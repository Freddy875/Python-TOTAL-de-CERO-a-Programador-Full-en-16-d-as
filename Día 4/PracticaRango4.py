# Inicializar la variable para la suma
suma_cuadrados = 0

# Recorrer los números del 1 al 15
for numero in range(1, 16):

    # Calcular el cuadrado del número
    cuadrado = numero ** 2

    # Acumular el cuadrado en la suma
    suma_cuadrados += cuadrado

    # Mostrar el cálculo y la suma acumulada
    print(f"{numero} al cuadrado = {cuadrado} | Suma acumulada = {suma_cuadrados}")

# Mostrar el resultado final
print(f"\nResultado final: {suma_cuadrados}")