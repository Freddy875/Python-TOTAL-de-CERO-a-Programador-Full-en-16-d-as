# ------------------------------------------------------------
# 1. Solicitar el nombre
# Se pide al usuario su nombre y se guarda en la variable
# "nombre".
# ------------------------------------------------------------

nombre = input("¿Cuál es tu nombre? ")


# ------------------------------------------------------------
# 2. Solicitar las ventas
# Se pregunta cuánto vendió el usuario durante este mes.
# Como input() devuelve un string, usamos float() para
# convertir la respuesta en un número decimal.
# ------------------------------------------------------------

ventas = float(input("¿Cuánto has vendido este mes? "))


# ------------------------------------------------------------
# 3. Calcular la comisión
# La comisión corresponde al 13% del total de las ventas.
# Para calcularla, multiplicamos las ventas por 13 y
# dividimos el resultado entre 100.
# ------------------------------------------------------------

comision = ventas * 50 / 100


# ------------------------------------------------------------
# 4. Mostrar el resultado
# Se muestra el nombre del vendedor, el total de ventas
# realizadas durante el mes y la comisión correspondiente.
# Los valores de ventas y comisión se muestran con dos
# posiciones decimales.
# ------------------------------------------------------------

print(f"{nombre}, este mes vendiste {ventas:.2f} y tu comisión por esas ventas es de {comision:.2f}")