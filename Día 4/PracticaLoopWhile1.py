# ------------------------------------------------------------
# Práctica Loop While 1
#
# Crea un Loop While que imprima en pantalla los números
# del 10 al 0, uno a la vez.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la variable inicial
#
# Se almacena el número 10 en la variable numero.
# Este será el valor inicial del conteo.
# ------------------------------------------------------------

numero = 10


# ------------------------------------------------------------
# Loop While para contar de 10 a 0
#
# while repite el bloque mientras numero sea mayor o igual
# que 0.
#
# print() muestra en pantalla el valor actual de numero.
#
# -= 1 resta 1 al valor de numero en cada iteración,
# permitiendo que el conteo avance de 10 hasta 0.
# ------------------------------------------------------------

while numero >= 0:
    print(numero)
    numero -= 1  # Restar 1 en cada iteración