# ------------------------------------------------------------
# Práctica Return 4
# Crear una función llamada usd_a_eur que reciba como único
# parámetro un monto en dólares y devuelva su equivalente
# en euros.
# Para esta práctica se utiliza la conversión:
# 1 USD = 0.90 EUR.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Definir la función para convertir USD a EUR
# Recibe el monto en dólares y lo multiplica por 0.90.
# return devuelve el resultado de la conversión.
# ------------------------------------------------------------

def usd_a_eur(dolares):
    return dolares * 0.90  # Conversión a euros


# ------------------------------------------------------------
# Pedir al usuario la cantidad de dólares
# El valor ingresado se convierte a decimal y se almacena
# en la variable dolares.
# ------------------------------------------------------------

dolares = float(input("¿Cuántos dólares quieres convertir a euros? "))


# ------------------------------------------------------------
# Calcular el monto en euros
# Se llama a la función y se le entrega la cantidad de
# dólares ingresada por el usuario.
# ------------------------------------------------------------

euros = usd_a_eur(dolares)


# ------------------------------------------------------------
# Mostrar el resultado
# Se muestra la cantidad de dólares ingresada y su equivalente
# en euros.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Mostrar el resultado
# Se muestran los dólares y el resultado de la conversión
# con exactamente 2 decimales.
# ------------------------------------------------------------

print(f"{dolares:.2f} USD equivalen a {euros:.2f} EUR")