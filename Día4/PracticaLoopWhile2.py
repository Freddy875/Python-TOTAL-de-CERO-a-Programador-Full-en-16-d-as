# ------------------------------------------------------------
# Práctica Loop While 2
#
# Crea un Loop While que reste de uno en uno los números
# desde el 50 hasta el 0, incluyendo ambos números.
#
# Si el número es divisible por 5, se debe mostrar en pantalla.
#
# Si el número no es divisible por 5, el loop continúa sin
# mostrar el número.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la variable inicial
#
# Se almacena el número 50 en la variable numero.
# Este será el valor inicial del conteo.
# ------------------------------------------------------------

numero = 50


# ------------------------------------------------------------
# Loop While para restar hasta 0
#
# while repite el bloque mientras numero sea mayor o igual
# que 0.
#
# El operador % obtiene el resto de la división.
# Si el resto de dividir numero entre 5 es 0, significa
# que el número es divisible por 5 y se muestra en pantalla.
# ------------------------------------------------------------

while numero >= 0:
    if numero % 5 == 0:  # Verificar si el número es divisible por 5
        print(numero)

    numero -= 1  # Restar 1 en cada iteración